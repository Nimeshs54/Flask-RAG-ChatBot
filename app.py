import os
from flask import Flask, request, render_template, jsonify
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

qa_chain = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global qa_chain
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
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

        # Set up the LLM and QA chain
        llm = Ollama(model="llama3.2")
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

        return jsonify({"message": "File uploaded and processed successfully"}), 200
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
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)