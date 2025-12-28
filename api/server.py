from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# اضافه کردن ریشه پروژه به PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.engine import DetectionEngine

app = FastAPI(title="AntiDDoS API")
engine = DetectionEngine()

class InspectRequest(BaseModel):
    ip: str

@app.get("/")
def root():
    return {"status": "AntiDDoS API is running"}

@app.post("/inspect")
def inspect(req: InspectRequest):
    return engine.inspect_ip(req.ip)

@app.get("/metrics")
def metrics():
    return engine.get_metrics()
