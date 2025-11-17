#!/usr/bin/env python3
"""
Function to compute descriptive statistics for DataFrame columns
"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except Timestamp

    Args:
        df: pd.DataFrame

    Returns:
        A new pd.DataFrame containing descriptive statistics
    """
    df_without_timestamp = df.drop(columns=['Timestamp'], errors='ignore')

    stats = df_without_timestamp.describe()

    return stats
