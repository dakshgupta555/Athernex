from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import uvicorn
import os

app = FastAPI()

def load_master():
    if not os.path.exists('golden_ref.jpg'): return None
    img = cv2.imread('golden_ref.jpg', cv2.IMREAD_GRAYSCALE)
    return cv2.resize(img, (400, 200))

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    master = load_master()
    if master is None: 
        return {"error": "golden_ref.jpg missing on server"}

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    upload_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    gray_upload = cv2.cvtColor(upload_img, cv2.COLOR_BGR2GRAY)
    gray_upload = cv2.resize(gray_upload, (400, 200))
    
    score, _ = ssim(master, gray_upload, full=True)
    
    # Return clearly labeled keys that the dashboard expects
    return {
        "authenticity": "GENUINE" if score > 0.85 else "SUSPICIOUS",
        "confidence": round(float(score), 3),
        "reason": "Structural similarity match" if score > 0.85 else "Geometry mismatch"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
