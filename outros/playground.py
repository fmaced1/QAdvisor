import yfinance as yf

from utils.tools import *
from utils._telegram import Bot
from utils.charts.charts import Charts
from utils.strategies.macd import Macd
from utils.ydownload import StockData

import pandas as pd

df_tickers_list = pd.read_csv("config/tickers.csv", sep=',')

"""stocks_df = Macd.macd_analisys(
    StockData.download(ticker, "3mo", "1wk"), ["R+"], 5)

#Charts.table_dataframe_to_jpeg(ticker, stocks_df)

Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")"""

#print(StockData.download_last_quote(ticker, (60*5)))

dict_ = {}

for i in range(0, len(df_tickers_list.index)):
    ticker = str("{0}.SA".format(df_tickers_list['tickers'][i]))
    df = StockData.get_info(ticker)
    dict_[ticker] = df["bookValue"]

df_ = pd.DataFrame.from_dict(dict_, orient='index', columns=['bookValue'])
df_.sort_values(by='bookValue', inplace=True)
pd.set_option('display.max_rows', df_.shape[0]+1)
print(df_)
