import yfinance as yf
import pandas as pd

import json

ticker = yf.Ticker("STBP3.SA")

print(json.dumps(ticker.info, indent=4))


"""stocks_df = Macd.macd_analisys(
    StockData.download(ticker, "3mo", "1wk"), ["R+"], 5)

#Charts.table_dataframe_to_jpeg(ticker, stocks_df)

Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")"""

#print(StockData.download_last_quote(ticker, (60*5)))
