from utils.cache.redis import RedisCache
import yfinance as yf
import simplejson as sjson
import json
import pandas as pd

class StockData(object):
    def get_history(self, ticker=str, period=str, interval=str, expiration_seconds=(60*60)*1):
        try:
            return RedisCache().get_value(ticker)
        except TypeError:
            data = yf.Ticker(ticker).history(period, interval, actions=False).dropna()
            RedisCache().set_value(ticker, data, expiration_seconds)
            
            return RedisCache().get_value(ticker)

    def get_info(self, ticker=str, expiration_seconds=(60*60)*1):
        ticker_info = "{}_{}".format(ticker, "info")
        try:
            return pd.DataFrame.from_dict(RedisCache().get_value(ticker_info), orient='index')[0]
        except TypeError:
            data = yf.Ticker(ticker).info
            RedisCache().set_value(ticker_info, data, expiration_seconds)
            
            return pd.DataFrame.from_dict(RedisCache().get_value(ticker_info), orient='index')[0]

    def get_last_quote(self, ticker, expiration_seconds):
        ticker_last_quote = "{}_{}".format(ticker, "last_quote")
        try:
            return RedisCache().get_value(ticker_last_quote)
        except TypeError:
            data = round(yf.Ticker(ticker).history(period="1d", interval="1d", actions=False).dropna().tail(1)['Close'].iloc[0], 2)
            RedisCache().set_value(ticker_last_quote, data, expiration_seconds)

            return RedisCache().get_value(ticker_last_quote)

    def save_json_into_redis(self, ticker=str, period="3mo", interval="1wk"):
        ticker_info = "{}_{}".format(ticker, "info")

        stocks_json = {}
        stocks_json["data"] = []
        stocks_json["ticker"] = ticker
        stocks_json["period"] = period
        stocks_json["interval"] = interval

        RedisCache().set_value(ticker_info, json.dumps(stocks_json))

        return RedisCache().get_value(ticker_info)
