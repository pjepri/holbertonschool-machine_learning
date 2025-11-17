#!/usr/bin/env python3
"""
Function to concatenate DataFrames with rearranged MultiIndex hierarchy
"""

import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Concatenates two DataFrames with Timestamp as first level of MultiIndex

    Args:
        df1: pd.DataFrame (coinbase)
        df2: pd.DataFrame (bitstamp)

    Returns:
        The concatenated pd.DataFrame with Timestamp as first level
    """
    df1 = index(df1)
    df2 = index(df2)

    df1_fil = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2_fil = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]

    res = pd.concat([df2_fil, df1_fil], keys=['bitstamp', 'coinbase'])

    res = res.swaplevel().sort_index()

    return res
