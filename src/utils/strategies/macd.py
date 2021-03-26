from stockstats import StockDataFrame as Sdf

class Macd:
    def __init__(self):
        pass

    def filter_by_macdh(stocks_df, signals_of_revert, candles, ticker, consider_tickers, ignore_tickers):
        stocks_df = Sdf.retype(stocks_df)
        """open_ = stocks_df['open']
        high = stocks_df['high']
        low = stocks_df['low']
        close = stocks_df['close']
        #adj_close = stocks_df['adj close']
        volume = stocks_df['volume']
        macd = stocks_df['macd']
        macds = stocks_df['macds']"""
        macdh = stocks_df['macdh']

        df = []

        if len(stocks_df.index) > candles:
            for i in range(0, len(stocks_df.index)):

                if macdh[i] == macdh[i - 1]:
                    df.append('{0}'.format("E"))
                elif  macdh[i] > macdh[i - 1] < macdh[i - 2] < macdh[i - 3] < macdh[i - 4]:
                    df.append('{0}'.format("R+"))
                elif macdh[i] > macdh[i - 1]:
                    df.append('{0}'.format("G+"))

                elif macdh[i] < macdh[i - 1] > macdh[i - 2] > macdh[i - 3] > macdh[i - 4]:
                    df.append('{0}'.format("R-"))
                elif macdh[i] < macdh[i - 1]:
                    df.append('{0}'.format("G-"))
                else:
                    df.append('{0}'.format("NULL"))

            stocks_df['macdh_a'] = df

            if (stocks_df['macdh_a'][-candles:].apply(lambda sentence: any(word in sentence for word in signals_of_revert))).any() and ticker not in ignore_tickers or ticker in consider_tickers:
                stocks_df = stocks_df.iloc[::-1]
                return stocks_df

        return None
