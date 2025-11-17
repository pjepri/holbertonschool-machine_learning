#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.drop(columns=['Weighted_Price'])

df = df.rename(columns={'Timestamp': 'Date'})

df = df.assign(Date=pd.to_datetime(df['Date'], unit='s'))

df = df.set_index('Date').copy()

df.loc[:, 'Close'] = df['Close'].ffill()

df.loc[:, 'High'] = df['High'].fillna(df['Close'])
df.loc[:, 'Low'] = df['Low'].fillna(df['Close'])
df.loc[:, 'Open'] = df['Open'].fillna(df['Close'])

df.loc[:, 'Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df.loc[:, 'Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

df_filtered = df[df.index >= '2017-01-01']

df_daily = df_filtered.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

print(df_daily)
