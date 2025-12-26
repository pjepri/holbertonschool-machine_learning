#!/usr/bin/env python3
"""Optimize k for K-means clustering"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    Tests for the optimum number of clusters by variance

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        kmin: positive integer, minimum number of clusters (inclusive)
        kmax: positive integer, maximum number of clusters (inclusive)
        iterations: positive integer, max iterations for K-means

    Returns:
        results: list of K-means outputs for each cluster size
        d_vars: list of variance differences from smallest cluster size
        or None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None

    n, d = X.shape

    if kmax is None:
        kmax = n

    if not isinstance(kmin, int) or kmin < 1:
        return None, None
    if not isinstance(kmax, int) or kmax < 1:
        return None, None
    if not isinstance(iterations, int) or iterations < 1:
        return None, None
    if kmin >= kmax:
        return None, None
    if kmax > n:
        return None, None

    results = []
    variances = []

    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        if C is None:
            return None, None
        results.append((C, clss))
        variances.append(variance(X, C))

    var_min = variances[0]
    d_vars = [var_min - v for v in variances]

    return results, d_vars
