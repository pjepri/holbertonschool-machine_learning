#!/usr/bin/env python3
"""Calculate intra-cluster variance"""
import numpy as np


def variance(X, C):
    """
    Calculates the total intra-cluster variance of a data set

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        C: numpy.ndarray of shape (k, d) containing the centroid means

    Returns:
        var: the total variance, or None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(C, np.ndarray) or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None

    # Compute distances between all points and all centroids (n, k)
    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)

    # Get minimum distance per point (to nearest centroid)
    min_distances = np.min(distances, axis=1)

    # Total variance is sum of squared minimum distances
    var = np.sum(min_distances ** 2)

    return var
