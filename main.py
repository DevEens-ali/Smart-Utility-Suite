from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health():
    return {'Status':'ok, backend is running'}