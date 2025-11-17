#!/usr/bin/env python3
"""
Function to fill missing values in DataFrame according to specific rules
"""


def fill(df):
    """
    Removes Weighted_Price column and fills missing values according to rules

    Args:
        df: pd.DataFrame

    Returns:
        The modified pd.DataFrame
    """

    df = df.drop(columns=['Weighted_Price'])

    df['Close'] = df['Close'].ffill()

    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    return df
