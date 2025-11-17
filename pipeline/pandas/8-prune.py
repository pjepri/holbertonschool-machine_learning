#!/usr/bin/env python3
"""
Function to remove entries where Close has NaN values
"""

import pandas as pd


def prune(df):
    """
    Removes any entries where Close has NaN values

    Args:
        df: pd.DataFrame

    Returns:
        The modified pd.DataFrame with NaN values in Close column removed
    """
    pruned_df = df.dropna(subset=['Close'])

    return pruned_df
