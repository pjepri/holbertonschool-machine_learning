#!/usr/bin/env python3
"""
Function to sort DataFrame in reverse chronological order and transpose it
"""


def flip_switch(df):
    """
    Sorts the data in reverse chronological order and transposes it

    Args:
        df: pd.DataFrame

    Returns:
        The transformed pd.DataFrame (sorted in reverse and transposed)
    """
    sorted_df = df.sort_index(ascending=False)

    transposed = sorted_df.T

    return transposed
