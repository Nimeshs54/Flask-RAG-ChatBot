import os
import pytest
from flask import json
from app import create_app
from io import BytesIO

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_index_page(client):
    """Test if the index page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200

def test_upload_without_file(client):
    """Test uploading without a file."""
    response = client.post("/upload", data={})
    assert response.status_code == 400
    assert response.json["error"] == "No file uploaded"

def test_upload_without_model(client):
    """Test uploading a file without selecting a model."""
    pdf_content = b"%PDF-1.4\n%Test PDF Content"
    data = {
        "file": (BytesIO(pdf_content), "test.pdf")
    }
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    
    assert response.status_code == 400
    assert response.json["error"] == "No model selected"

def test_upload_valid_pdf(client):
    """Test uploading a valid PDF with a selected model."""
    pdf_path = os.path.join("uploads", "test.pdf")

    with open(pdf_path, "rb") as pdf_file:
        data = {
            "file": (pdf_file, "test.pdf"),
            "model": "llama3.2"
        }
        response = client.post("/upload", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert response.json["message"] == "File uploaded and processed successfully"
    assert response.json["model"] == "llama3.2"

def test_query_without_question(client):
    """Test querying the system without providing a question."""
    response = client.post("/query", json={})
    assert response.status_code == 400
    assert response.json["error"] == "Please upload a document first"


def test_query_without_upload(client):
    """Test querying before uploading a document."""
    response = client.post("/query", json={"question": "What is AI?"})
    assert response.status_code == 400
    assert response.json["error"] == "Please upload a document first"

def test_upload_with_invalid_file(client):
    """Test uploading a non-PDF file."""
    txt_content = b"Test text file content"
    data = {
        "file": (BytesIO(txt_content), "test.txt"),
        "model": "llama3.2"
    }
    response = client.post("/upload", data=data, content_type="multipart/form-data")
    
    assert response.status_code == 400
    assert response.json["error"] == "Only PDF files are supported"
