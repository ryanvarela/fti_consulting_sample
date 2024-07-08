from fastapi import FastAPI, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from app.alpha_vantage_client import get_intraday_data
from app.security import get_api_key

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FTI Consulting Sample API."}

@app.get("/intraday/{symbol}")
def get_intraday(symbol: str, api_key: str = Depends(get_api_key)):
    data = get_intraday_data(symbol)
    return data