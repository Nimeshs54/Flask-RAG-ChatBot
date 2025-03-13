import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Function to create a Flask app instance
def create_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Global variables
    global qa_chain, selected_model
    qa_chain = None
    selected_model = None

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        global qa_chain, selected_model
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        selected_model = request.form.get('model')  # Get selected model from form
        if not selected_model:
            return jsonify({"error": "No model selected"}), 400

        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Process the PDF
            loader = PyPDFLoader(filepath)
            documents = loader.load()

            # Split documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(documents)

            # Create embeddings and vector store
            embeddings = OllamaEmbeddings(model="llama3.2")
            vectorstore = Chroma.from_documents(texts, embeddings)

            # Set up the LLM based on user selection
            if selected_model == "llama3.2":
                llm = Ollama(model="llama3.2")
            elif selected_model == "deepseek-r1-distill-qwen-32b":
                groq_api_key = os.getenv("GROQ_API_KEY")
                if not groq_api_key:
                    return jsonify({"error": "GROQ_API_KEY not found in .env"}), 500
                llm = ChatGroq(
                    groq_api_key=groq_api_key,
                    model_name="deepseek-r1-distill-qwen-32b"
                )
            else:
                return jsonify({"error": "Invalid model selected"}), 400

            prompt_template = """Use the following pieces of context to answer the question. If you don't know the answer, say so.
            Context: {context}
            Question: {question}
            Answer: """
            prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vectorstore.as_retriever(),
                chain_type_kwargs={"prompt": prompt}
            )

            return jsonify({"message": "File uploaded and processed successfully", "model": selected_model}), 200
        else:
            return jsonify({"error": "Only PDF files are supported"}), 400

    @app.route('/query', methods=['POST'])
    def query():
        if qa_chain is None:
            return jsonify({"error": "Please upload a document first"}), 400
        
        question = request.json.get('question')
        if not question:
            return jsonify({"error": "No question provided"}), 400
        
        # Get the answer from the QA chain
        result = qa_chain({"query": question})
        answer = result["result"]
        return jsonify({"answer": answer, "model": selected_model})

    return app

if __name__ == '__main__':
    create_app().run(debug=True)