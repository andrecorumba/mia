"""
This is the main API file.

To run the API, use the following command:
uvicorn view.api:api --reload

To API documentation, go to the following URL:
http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse

api = FastAPI()

@api.get("/")
def read_root():
    """This is the root path"""
    # return {"FastAPI": "Running"}
    return JSONResponse(content={"FastAPI": "Running"})

@api.post("/upload/")
async def create_upload_file(file: UploadFile = None):
    """This path receives a single file"""
    return {"filename": file.filename}

@api.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    """This path receives a list of files"""
    return {"filenames": [file.filename for file in files]}

@api.post("/run/")
async def run_chain(file: UploadFile, background_tasks: BackgroundTasks):
    """This path receives a single file and process it"""
    background_tasks.add_task(load_file, file)
    return {"message": "File is being processed"}


def load_file(file: UploadFile):
    """This function processes the  file"""
    print(f"Processing file {file.filename}")

@api.post("/run-files/")
async def run_chain_files(files: list[UploadFile], background_tasks: BackgroundTasks):
    """This path receives a list of files and process them"""
    background_tasks.add_task(load_files, files)
    return {"message": "Files are being processed"}

def load_files(files: list[UploadFile]):
    """This function processes the files"""
    print(f"Processing files {files}")



# TODO: Add path to receive response from processing pdf file