import pandas as pd
import json

from utils.cache.redis import RedisCache
from utils.ydownload import StockData
from utils.strategies.macd import Macd

class Recomendations(object):
    def __init__(self):
        self.df_tickers_list = pd.read_csv("config/tickers.csv", sep=',')
        self.ignore_tickers = ""   #["CSNA3.SA", "USIM5.SA"]
        self.consider_tickers = "" #["COGN3.SA", "MGLU3.SA"]
        self.period = "1y"
        self.interval = "1wk"
        self.candles = 3
        self.signals_of_revert = ["R+", "R-"]
        self.expiration_seconds = (60*60)*1

    def get_from_redis(self, ticker=str):
        _ticker = "{}_{}".format(ticker, "recomendations")

        try:
            return RedisCache().get_value(_ticker)
        except TypeError:
            stocks_df = Macd.macd_analisys(
                StockData().get_history(ticker, self.period, self.interval), 
                self.signals_of_revert,
                self.candles,
                ticker,
                self.consider_tickers,
                self.ignore_tickers
            )
            if isinstance(stocks_df, pd.DataFrame):
                RedisCache().set_value(_ticker, stocks_df.sort_index(ascending=False).head(1), self.expiration_seconds)
                return RedisCache().get_value(_ticker).sort_index(ascending=False).head(1)
            else:
                return None

    def get(self, output='json'):
        data_json = {}
        df = pd.DataFrame()

        for i in range(0, len(self.df_tickers_list.index)):
            ticker = str("{0}.SA".format(self.df_tickers_list['tickers'][i]))

            df_recomendations = self.get_from_redis(ticker=ticker)

            if output == "json" and isinstance(df_recomendations, pd.DataFrame):
                data_json[ticker] = json.loads(df_recomendations.to_json(orient="records"))

            if output == "dataframe" and isinstance(df_recomendations, pd.DataFrame):
                df_recomendations["ticker"] = ticker
                df = df.append(df_recomendations)

        if output == "json":
            return data_json
        
        if output == "dataframe":
            return df