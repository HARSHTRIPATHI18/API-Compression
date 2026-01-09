from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/large")
def large_payload():
    # Create large JSON response
    data = [{"id": i, "name": f"user_{i}", "description": "x" * 200} for i in range(5000)]
    return {"count": len(data), "data": data}

@app.get("/api/health")
def health():
    return {"status": "ok"}
