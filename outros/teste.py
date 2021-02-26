import pandas as pd

source = pd.DataFrame({'Symbol' : ['APPL', 'APPL', 'APPL','APPL'], 
                  'Type' : ['sell', 'buy', 'buy', 'sell'],
                  'Total' : ['1','2','3','4']})

print(source)
source.groupby(["Symbol", "Type"]).cumsum()
print(source)