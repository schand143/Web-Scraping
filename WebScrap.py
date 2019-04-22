import pandas as pd 
tables = pd.read_html("http://www.moneycontrol.com/financials/rico%20auto/balance-sheetVI/RA04") 
df=tables[3] 
df.to_csv('abc1.csv') 
print(tables[3])