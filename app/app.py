import pandas as pd
import streamlit as st
from PIL import Image

from utils.tools import Cronometer, remove_files_in_folder, remove_file
from utils.ydownload import StockData
from utils.strategies.macd import Macd
from utils.charts.charts import Charts
from config.config import *

def display_macdh_analysis(ticker, period, interval, signals_of_revert, candles, consider_tickers, ignore_tickers):
    stocks_df = Macd.filter_by_macdh(
        StockData().get_history(ticker, period, interval),
        signals_of_revert,
        candles,
        ticker,
        consider_tickers,
        ignore_tickers
    )

    if isinstance(stocks_df, pd.DataFrame) and not stocks_df.empty:
        with st.expander(f"Detalhes para {ticker}"):
            st.subheader("Price:")
            st.line_chart(stocks_df["close"])
            
            st.subheader("MACDh:")
            st.area_chart(stocks_df["macdh"])
            
            st.subheader("Dataframe:")
            st.dataframe(stocks_df.style.highlight_min(axis=0, color='red'))

def display_analysis_report(ticker, period, interval, signals_of_revert, candles, consider_tickers, ignore_tickers):
    stocks_df = Macd.filter_by_macdh(
        StockData().get_history(ticker, period, interval),
        signals_of_revert,
        candles,
        ticker,
        consider_tickers,
        ignore_tickers
    )

    if isinstance(stocks_df, pd.DataFrame) and not stocks_df.empty:
        with st.expander(f"Relatório para {ticker}"):
            filename = Charts.candlestick_chart(ticker, stocks_df, extension_type="jpeg")
            image = Image.open(filename)
            st.image(image, caption=f'Ticker: {ticker}', use_column_width=True)

def main():
    start_time = Cronometer().start_cronometer()

    remove_files_in_folder(folders_to_cleanup)
    remove_file("analisys.txt")

    st.sidebar.title('FinAdvisor :sunglasses:')

    add_selectbox = st.sidebar.selectbox(
        "Selecione o indicador para filtrar:",
        ["Filter by MACDH", "Analisys Report"]
    )

    for _, row in df_tickers_list.iterrows():
        ticker = f"{row['tickers']}.SA"

        if add_selectbox == "Filter by MACDH":
            #st.header("Filtrando ações pela estratégia MACDH")
            display_macdh_analysis(ticker, period, interval, signals_of_revert, candles, consider_tickers, ignore_tickers)
        elif add_selectbox == "Analisys Report":
            #st.header("Relatórios gerados no Plotly - Estratégia MACDH")
            display_analysis_report(ticker, period, interval, signals_of_revert, candles, consider_tickers, ignore_tickers)

    elapsed_time = Cronometer().stop_cronometer(start_time)
    st.write(f"Tempo total da execução: {elapsed_time}")

if __name__ == "__main__":
    main()