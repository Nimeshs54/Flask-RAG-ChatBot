# Flask-RAG-ChatBot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green?style=flat-square&logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-0.3.0-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

A sleek, AI-powered web application for chatting with PDF documents using Llama 3.2 (via Ollama) or DeepSeek R1 Distill Qwen 32B (via Groq API) with LangChain's RAG capabilities.

## ✨ Features
- **PDF Upload**: Upload PDFs to process their content.
- **Model Selection**: Choose between Llama 3.2 or DeepSeek R1 Distill Qwen 32B.
- **AI Chat**: Ask questions and get responses based on the document.
- **Modern UI**: Professional interface with model selection and chat display.

## 🛠️ Tech Stack
| Component           | Technology                              |
|---------------------|-----------------------------------------|
| **Web Framework**   | Flask                                   |                
| **LLM Integration** | LangChain, Ollama, Groq API             |
| **Models**          | Llama 3.2, DeepSeek R1 Distill Qwen 32B |
| **Vector Store**    | Chroma                                  |
| **PDF Processing**  | PyPDF2                                  |
| **Frontend**        | HTML, CSS, JS                           |

## 📦 Installation

### Prerequisites
- **Python 3.8+**
- **Ollama**: For Llama 3.2:
  ```bash
  ollama pull llama3.2
  ollama serve

---

## Groq API Key
For DeepSeek R1, sign up at [console.groq.com](https://console.groq.com) and add your API key to the `.env` file:

```plaintext
GROQ_API_KEY='your-api-key-here'
```

---

## Steps

### Clone the Repository
```bash
git clone https://github.com/Nimeshs54/Flask-RAG-ChatBot.git
cd Flask-RAG-ChatBot
```

### Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```

Open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🚀 Usage
1. Select either **"Llama 3.2"** or **"DeepSeek R1 Distill Qwen 32B"** from the dropdown.
2. Upload a PDF and wait for processing.
3. Ask questions in the chat interface and receive responses from your chosen model.

---

## 📊 Results

### **Llama 3.2 Model**
**Example Query**:  
_"What is this document about?"_

**Llama 3.2 Response**:  
![Llama 3.2 Result](https://github.com/user-attachments/assets/3213c4d4-cd5a-407c-b3d0-8deabf3f1e0e)

---

### **DeepSeek R1 Distill Qwen 32B Model**
**Example Query**:  
_"What is this document about?"_

**DeepSeek R1 Distill Qwen 32B Response**:  
![DeepSeek R1 Distill Qwen 32B Result](https://github.com/user-attachments/assets/81425858-7871-474d-8776-7cb54aa3b7f2)
