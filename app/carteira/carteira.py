import pandas as pd
import numpy as np

df = pd.read_csv("app/carteira/carteira.csv", delimiter=";", parse_dates=["Date"])

df["Turnover"] = (df["Quantity"] * df["Amount per unit"])
""" Se o type for sell inverte o sinal do total para negativo
carteira["Total"] = np.where(carteira["Type"] == "sell", (carteira["Units"] * carteira["Price"]) * -1, carteira["Total"])
carteira["Units"] = np.where(carteira["Type"] == "sell", carteira["Units"] * -1, carteira["Units"])

carteira["Units_buy"]  = np.where([carteira["Type"] == "buy" & carteira["Stock"] == "STBP3" ], carteira["Units"] * -1, carteira["Units"])"""

df.sort_values(['Symbol','Date','Type'], ascending=[True, True, True], inplace=True)
# your code
df['Adjusted Quantity'] = df.apply(lambda x: ((x.Type == "buy") - (x.Type == "sell")) * x['Quantity'], axis = 1)
df['Adjusted Quantity'] = df.groupby('Symbol')['Adjusted Quantity'].cumsum()
df['Adjusted Price Per Unit'] = df.apply(lambda x: ((x.Type == "buy") - (x.Type == "sell")) * x['Turnover'], axis = 1)
df['Adjusted Price Per Unit'] = df.groupby('Symbol')['Adjusted Price Per Unit'].cumsum().div(df['Adjusted Quantity'])



df.loc[df['Type'] == 'sell',['Adjusted Price Per Unit']] = np.NaN
df.fillna(method='ffill', inplace=True)

print(df)