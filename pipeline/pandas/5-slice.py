#!/usr/bin/env python3
"""
Function to slice DataFrame by selecting specific columns and every 60th row
"""


def slice(df):
    """
    Extracts specific columns and selects every 60th row

    Args:
        df: pd.DataFrame

    Returns:
        The sliced pd.DataFrame with High, Low, Close, Volume_(BTC) columns
        and every 60th row
    """
    selected = df[['High', 'Low', 'Close', 'Volume_(BTC)']]

    sliced = selected.iloc[::60]

    return sliced
