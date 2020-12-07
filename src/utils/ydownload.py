from src.utils.redis import CacheStore
import yfinance as yf
import simplejson as json

class StockData:

    def download(ticker=str, period=str, interval=str, expiration_seconds=(60*60)*1):
        try:
            """Return data from cache, the expiration time is 1h"""
            return CacheStore.get_redis(ticker)
        except TypeError:
            data = yf.Ticker(ticker).history(period, interval, actions=False).dropna()
            CacheStore.set_redis(ticker, data, expiration_seconds)
            
            return CacheStore.get_redis(ticker)

    def download_info_json(ticker=str, expiration_seconds=(60*60)*1):
        ticker_info = "{}_{}".format(ticker, "info")
        try:
            """Return data from cache, the expiration time is 1h"""
            return json.dump(CacheStore.get_redis(ticker_info), indent=4)
        except TypeError:
            data = yf.Ticker(ticker).info
            CacheStore.set_redis(ticker_info, data, expiration_seconds)
            
            return json.load(CacheStore.get_redis(ticker_info), indent=4)

    def download_last_quote(ticker, expiration_seconds):
        ticker_last_quote = "{}_{}".format(ticker, "last_quote")
        try:
            return CacheStore.get_redis(ticker_last_quote)
        except TypeError:
            data = round(yf.Ticker(ticker).history(period="1d", interval="1d", actions=False).dropna().tail(1)['Close'].iloc[0], 2)
            CacheStore.set_redis(ticker_last_quote, data, expiration_seconds)

            return CacheStore.get_redis(ticker_last_quote)

    def save_json_into_redis(ticker=str, period="3mo", interval="1wk"):
        """TODO Save Json Object into redis"""
        stocks_json = {}
        stocks_json["data"] = []
        stocks_json["ticker"] = ticker
        stocks_json["period"] = period
        stocks_json["interval"] = interval

        CacheStore.set_redis("{0}_info".format(ticker), json.dumps(stocks_json))

        return CacheStore.get_redis("{0}_info".format(ticker))
