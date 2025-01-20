import fastapi

app = fastapi.FastAPI()

@app.get("/health")
async def root():
    """
    Sample curl request:
    curl -X 'GET' \
      'http://127.0.0.1:8080/health' \
      -H 'accept: application/json'
    """
    return {"status": 200}