from stockstats import StockDataFrame as Sdf
import pandas as pd

class Macd:
    @staticmethod
    def filter_by_macdh(
        stocks_df: pd.DataFrame, 
        signals_of_revert: list, 
        candles: int, 
        ticker: str, 
        consider_tickers: list, 
        ignore_tickers: list
    ) -> pd.DataFrame:
        """
        Filters stocks based on the MACD Histogram (MACDH) divergence.

        Args:
            stocks_df (pd.DataFrame): DataFrame containing stock data.
            signals_of_revert (list): List of reversal signals to filter by.
            candles (int): Number of candles to consider in the filter.
            ticker (str): The stock ticker symbol.
            consider_tickers (list): List of tickers to consider in the filter.
            ignore_tickers (list): List of tickers to ignore in the filter.

        Returns:
            pd.DataFrame: Filtered DataFrame, or None if no match is found.
        """

        stocks_df = Sdf.retype(stocks_df)
        macdh = stocks_df['macdh']
        macdh_signals = []

        if len(stocks_df.index) > candles:
            for i in range(1, len(stocks_df.index)):
                if macdh.iloc[i] == macdh.iloc[i - 1]:
                    macdh_signals.append("E")
                elif (macdh.iloc[i] > macdh.iloc[i - 1] < macdh.iloc[i - 2] < macdh.iloc[i - 3] < macdh.iloc[i - 4]):
                    macdh_signals.append("R+")
                elif macdh.iloc[i] > macdh.iloc[i - 1]:
                    macdh_signals.append("G+")
                elif (macdh.iloc[i] < macdh.iloc[i - 1] > macdh.iloc[i - 2] > macdh.iloc[i - 3] > macdh.iloc[i - 4]):
                    macdh_signals.append("R-")
                elif macdh.iloc[i] < macdh.iloc[i - 1]:
                    macdh_signals.append("G-")
                else:
                    macdh_signals.append("NULL")

            stocks_df['macdh_a'] = ["NULL"] + macdh_signals

            if (stocks_df['macdh_a'].iloc[-candles:].apply(lambda x: any(sig in x for sig in signals_of_revert)).any() and 
                ticker not in ignore_tickers) or (ticker in consider_tickers):
                return stocks_df.iloc[::-1]

        return None