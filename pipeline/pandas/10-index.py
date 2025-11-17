#!/usr/bin/env python3
"""
Function to set Timestamp column as the index of the DataFrame
"""

import pandas as pd


def index(df):
    """
    Sets the Timestamp column as the index of the dataframe

    Args:
        df: pd.DataFrame

    Returns:
        The modified pd.DataFrame with Timestamp as index
    """
    df = df.set_index('Timestamp')

    return df
