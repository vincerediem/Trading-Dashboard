import pandas as pd
import numpy as np

AAPL = './Source Data/AAPL.csv'
AAPL = pd.read_csv(AAPL)
MSFT = pd.read_csv('./Source Data/MSFT.csv')
GOOGL = pd.read_csv('./Source Data/GOOGL.csv')
META = pd.read_csv('./Source Data/META.csv')
AMZN = pd.read_csv('./Source Data/AMZN.csv')
NFLX = pd.read_csv('./Source Data/NFLX.csv')
NVDA = pd.read_csv('./Source Data/NVDA.csv')

stocks = [AAPL, MSFT, GOOGL, META, AMZN, NFLX, NVDA]
stock_names = ['AAPL', 'MSFT', 'GOOGL', 'META', 'AMZN', 'NFLX', 'NVDA']

for i, name in enumerate(stock_names):
    #stock1 = stock.iloc[:, [0, 4]] ### used for practice selection
    stocks[i] = stocks[i][['Date', 'Close']]
    stocks[i].columns = ['Date', f'Close_{name}']

#print(stocks[3])

all_stocks = stocks[0]
for i in stocks[1:]:
    all_stocks = pd.merge(all_stocks, i, how='left', on='Date')

print(all_stocks.head())