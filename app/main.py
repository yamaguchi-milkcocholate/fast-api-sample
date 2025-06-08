import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Request

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_KEY")


def verify_api_key(request: Request):
    api_key = request.headers.get("X-API-KEY")
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True


@app.get("/", dependencies=[Depends(verify_api_key)])
async def read_root():
    return {"message": "Hello, World!"}
