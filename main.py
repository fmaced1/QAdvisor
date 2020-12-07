import pandas as pd

from src.utils.tools import *
from src.utils._telegram import Bot
from src.utils.ydownload import StockData
from src.utils.strategies.macd import Macd
from src.utils.charts.charts import Charts

""" Cronometer
from timeit import default_timer as timer
from datetime import timedelta
start = timer()"""

"""TODO Config - arquivo de config"""
df_tickers_list = pd.read_csv("app/config/tickers.csv", sep=',')
ignore_tickers = ""     #["CSNA3.SA", "USIM5.SA"]
period = "6mo"
interval = "1wk"
candles = 5
signals_of_revert = ["R+"]

"""Cleanup folders"""
folders_to_cleanup = ["app/charts/html/", "app/charts/jpeg/"]
remove_files_in_folder(folders_to_cleanup)
remove_file("analisys.txt")

for i in range(0, len(df_tickers_list.index)):

    ticker = str("{0}.SA".format(df_tickers_list['tickers'][i]))

    stocks_df = Macd.macd_analisys(
        StockData.download(ticker, period, interval), 
        signals_of_revert, 
        candles
    )

    if isinstance(stocks_df, pd.DataFrame) and ticker not in ignore_tickers:
        print(ticker)
        filename = Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")

        """ Send reports via Telegram"""
        #if filename is not None:
        #    Bot().send_photo(filename)

        init_logging().info("ticker: {}".format(ticker))

""" Cronometer
end = timer()
print(timedelta(seconds=end-start))"""