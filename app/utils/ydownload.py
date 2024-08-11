from utils.cache.redis import RedisCache
import yfinance as yf
import json
import pandas as pd

class StockData:
    def __init__(self):
        self.redis_cache = RedisCache()

    def _get_or_set_cache(self, key: str, fetch_function, expiration_seconds: int):
        value = self.redis_cache.get_value(key)
        if value is not None:
            return value
        
        data = fetch_function()
        self.redis_cache.set_value(key, data, expiration_seconds)
        return data

    def get_history(self, ticker: str, period: str, interval: str, expiration_seconds: int = 60*60) -> pd.DataFrame:
        def fetch_data():
            return yf.Ticker(ticker).history(period=period, interval=interval, actions=False).dropna()

        return self._get_or_set_cache(ticker, fetch_data, expiration_seconds)

    def get_info(self, ticker: str, expiration_seconds: int = 60*60) -> pd.Series:
        ticker_info = f"{ticker}_info"

        def fetch_data():
            return yf.Ticker(ticker).info

        data = self._get_or_set_cache(ticker_info, fetch_data, expiration_seconds)
        return pd.Series(data)

    def get_last_quote(self, ticker: str, expiration_seconds: int = 60*60) -> float:
        ticker_last_quote = f"{ticker}_last_quote"

        def fetch_data():
            return round(
                yf.Ticker(ticker).history(period="1d", interval="1d", actions=False).dropna().tail(1)['Close'].iloc[0], 2
            )

        return self._get_or_set_cache(ticker_last_quote, fetch_data, expiration_seconds)

    def save_json_into_redis(self, ticker: str, period: str = "3mo", interval: str = "1wk") -> str:
        ticker_info = f"{ticker}_info"

        stocks_json = {
            "data": [],
            "ticker": ticker,
            "period": period,
            "interval": interval
        }

        self.redis_cache.set_value(ticker_info, json.dumps(stocks_json))
        return self.redis_cache.get_value(ticker_info)