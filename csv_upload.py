from fastapi import APIRouter, File, UploadFile, HTTPException
import pandas as pd
import io
import os

router = APIRouter()

# 保存先ディレクトリ
UPLOAD_DIRECTORY = "./uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
    
    return {"filename": file.filename, "message": "File uploaded successfully"}

@router.get("/get-csv/{filename}")
async def get_csv(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    df = pd.read_csv(file_path)
    return df.head(1).to_dict(orient="records")
