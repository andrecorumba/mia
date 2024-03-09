"""
Tests to check if the API is working as expected.
"""

from fastapi.testclient import TestClient

from view.api_mia import api

client = TestClient(app=api)

def test_create_upload_file():
    """Test if the endpoint /upload/ is working as expected."""

    # Create a file to be uploaded
    file_content = b"This is a file that will be uploaded. Not a string."
    files = {"file": ("testfile.txt", file_content, "text/plain")}
    
    response = client.post("/upload/", files=files)
    
    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"filename": "testfile.txt"}

def test_create_upload_files():
    """Test if the endpoint /uploadfiles/ is working as expected."""

    # Create a list of files to be uploaded
    file_content = b"This is a file that will be uploaded. Not a string."

    files = [
        ("files", ("file1.txt", file_content, "text/plain")),
        ("files", ("file2.txt", file_content, "text/plain")),
    ]

    response = client.post("/uploadfiles/", files=files)
    
    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"filenames": ["file1.txt", "file2.txt"]}

def test_run_chain():
    """Test if the endpoint /run/ is working as expected."""

    # Create a file to be uploaded
    file_content = b"This is a file that will be uploaded. Not a string."
    files = {"file": ("testfile.txt", file_content, "text/plain")}
    
    response = client.post("/run/", files=files)
    
    # Verify the response
    assert response.status_code == 200
    assert response.json() == {"message": "File is being processed"}
