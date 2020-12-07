import yfinance as yf

from src.utils.tools import Tools as t
from src.utils.bot_telegram import Bot
from src.utils.charts.charts import Charts
from src.utils.strategies.macd import Macd
from src.utils.ydownload import StockData

ticker = "GGBR4.SA"

"""stocks_df = Macd.macd_analisys(
    StockData.download(ticker, "3mo", "1wk"), ["R+"], 5)

#Charts.table_dataframe_to_jpeg(ticker, stocks_df)

Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")"""

#print(StockData.download_last_quote(ticker, (60*5)))

print(StockData.download_info_json(ticker))
