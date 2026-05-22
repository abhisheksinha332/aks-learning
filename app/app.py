from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AKS CI/CD Demo",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}