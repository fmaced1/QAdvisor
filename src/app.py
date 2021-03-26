import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from utils.tools import Cronometer, remove_files_in_folder, remove_file
from utils.telebot import Telebot
from utils.ydownload import StockData
from utils.strategies.macd import Macd
from utils.charts.charts import Charts
from config.config import *

start_time = Cronometer().start_cronometer()

remove_files_in_folder(folders_to_cleanup)
remove_file("analisys.txt")

st.sidebar.title('FinAdvisor :sunglasses:')

add_selectbox = st.sidebar.selectbox(
    "Selecione o indicador para filtrar:",
    (["Filter by MACDH", "Analisys Report"])
)

if add_selectbox == "Filter by MACDH":
    st.header("Filtrando acoes pela estrategia MACDH")

    for i in range(0, len(df_tickers_list.index)):
        ticker = str("{0}.SA".format(df_tickers_list['tickers'][i]))

        stocks_df = Macd.filter_by_macdh(
            StockData().get_history(ticker, period, interval), 
            signals_of_revert,
            candles,
            ticker,
            consider_tickers,
            ignore_tickers)

        if isinstance(stocks_df, pd.DataFrame):
            st.subheader(df_tickers_list['tickers'][i])
            price = stocks_df["close"]
            macdh = stocks_df["macdh"]

            st.subheader("Preço:")
            st.line_chart(price)
            st.subheader("MACDH:")
            st.area_chart(macdh)
            st.subheader("Dataframe:")
            st.dataframe(stocks_df.style.highlight_min(axis=0, color='red'))

if add_selectbox == "Analisys Report":
    st.header("Reports gerados no plotly - Estrategia MACDH")

    for i in range(0, len(df_tickers_list.index)):
        ticker = str("{0}.SA".format(df_tickers_list['tickers'][i]))

        stocks_df = Macd.filter_by_macdh(
            StockData().get_history(ticker, period, interval), 
            signals_of_revert, 
            candles,
            ticker,
            consider_tickers,
            ignore_tickers
        )

        if isinstance(stocks_df, pd.DataFrame):
            st.subheader(df_tickers_list['tickers'][i])

            filename = Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")

            image = Image.open(filename)
            st.image(image, caption='Ticker: {}'.format(ticker), use_column_width=True)


print("Tempo total da execucao {}".format(Cronometer().stop_cronometer(start_time)))