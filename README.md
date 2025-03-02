# Flask-RAG-ChatBot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green?style=flat-square&logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-0.3.0-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/document-chatbot?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/yourusername/document-chatbot?style=flat-square)

A sleek, AI-powered web application that lets you upload a PDF document and chat with its contents using the Llama 3.2 model via Ollama, enhanced by LangChain's Retrieval-Augmented Generation (RAG) capabilities. Built with Flask, this tool offers a professional UI and seamless document querying experience.

---

## ✨ Features

- **PDF Upload**: Upload any PDF document to extract and process its content.
- **AI Chat**: Ask questions about the document and get contextual answers powered by Llama 3.2.
- **Modern UI**: A clean, professional interface with smooth animations and a responsive design.
- **RAG Pipeline**: Combines document retrieval and generation for accurate, context-aware responses.
- **Local LLM**: Runs entirely locally with Ollama, ensuring privacy and control.

---

## 🛠️ Tech Stack

| Component           | Technology         |
|---------------------|--------------------|
| **Web Framework**   | Flask              |
| **LLM Integration** | LangChain, Ollama  |
| **Model**           | Llama 3.2          |
| **Vector Store**    | Chroma             |
| **PDF Processing**  | PyPDF2             |
| **Frontend**        | HTML, CSS, JS      |

---

## 📦 Installation

### Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **Ollama**: Install Ollama and pull the Llama 3.2 model:
  ```bash
  ollama pull llama3.2
  ollama serve

---

## Steps
### Clone the Repository
  ```bash
  git clone https://github.com/Nimeshs54/Flask-RAG-ChatBot.git
  cd Flask-RAG-ChatBot
  ```

---

### Set Up a Virtual Environment
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

### Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```

---

### Run the Application
  ```bash
  python app.py
  ```

### Access the Application

Open your browser and navigate to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Usage

### 1. Upload a PDF
On the homepage, select a PDF file and click "Upload Document."

### 2. Chat with the Document
Once processed, a chat interface appears. Type your questions and get answers based on the document's content.

### 3. Enjoy
Experience fast, accurate responses with a professional-grade UI.

