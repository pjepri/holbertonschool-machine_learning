#!/usr/bin/env python3
"""
Function to convert DataFrame columns to numpy array
"""

import pandas as pd


def array(df):
    """
    Selects the last 10 rows of High and Close columns and
    converts to numpy array

    Args:
        df: pd.DataFrame containing columns named High and Close

    Returns:
        numpy.ndarray with the last 10 rows of High and Close columns
    """

    selected = df[['High', 'Close']].tail(10)

    arr = selected.values

    return arr
