#!/usr/bin/env python3
"""
Function to sort DataFrame by High price in descending order
"""

import pandas as pd


def high(df):
    """
    Sorts the DataFrame by High price in descending order

    Args:
        df: pd.DataFrame

    Returns:
        The sorted pd.DataFrame
    """
    sorted_df = df.sort_values(by='High', ascending=False)

    return sorted_df
