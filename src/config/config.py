import pandas as pd

df_tickers_list     = pd.read_csv("config/tickers.csv", sep=',')
ignore_tickers      = ""     #["CSNA3.SA", "USIM5.SA"]
consider_tickers    = ["COGN3.SA", "MGLU3.SA", "VVAR3.SA"]
period              = "1y"
interval            = "1wk"
candles             = 3
signals_of_revert   = ["R+"]

folders_to_cleanup  = ["charts/html/", "charts/jpeg/"]