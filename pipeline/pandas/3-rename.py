#!/usr/bin/env python3
"""
Function to rename Timestamp column and convert to datetime
"""

import pandas as pd


def rename(df):
    """
    Renames Timestamp column to Datetime, converts to datetime,
    and returns only Datetime and Close columns

    Args:
        df: pd.DataFrame containing a column named Timestamp

    Returns:
        The modified pd.DataFrame with only Datetime and Close columns
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})

    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')

    df = df[['Datetime', 'Close']]

    return df
