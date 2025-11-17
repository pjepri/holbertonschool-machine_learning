#!/usr/bin/env python3
"""
Function to create a pandas DataFrame from a numpy array
"""

import numpy as np
import pandas as pd


def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray
    
    Args:
        array: np.ndarray from which to create the pd.DataFrame
        
    Returns:
        pd.DataFrame with columns labeled in alphabetical order (A, B, C, ...)
    """
    num_cols = array.shape[1]
    
    columns = [chr(65 + i) for i in range(num_cols)]  
    
    df = pd.DataFrame(array, columns=columns)
    
    return df
