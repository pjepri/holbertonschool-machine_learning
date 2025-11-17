#!/usr/bin/env python3
"""
Function to concatenate two DataFrames with specific filtering and keys
"""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenates two DataFrames with specific filtering and keys

    Args:
        df1: pd.DataFrame (coinbase)
        df2: pd.DataFrame (bitstamp)

    Returns:
        The concatenated pd.DataFrame with keys
    """
    df1 = index(df1)
    df2 = index(df2)

    df2_filtered = df2[df2.index <= 1417411920]

    result = pd.concat([df2_filtered, df1], keys=['bitstamp', 'coinbase'])

    return result
