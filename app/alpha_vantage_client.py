import os
import requests
from dotenv import load_dotenv

load_dotenv()

ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("API_KEY")

def get_intraday_data(symbol: str, interval: str = "5min"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_API_URL, params=params)
    return response.json()