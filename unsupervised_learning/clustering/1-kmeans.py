#!/usr/bin/env python3
"""K-means clustering algorithm"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """
    Performs K-means on a dataset

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
           n is the number of data points
           d is the number of dimensions for each data point
        k: positive integer containing the number of clusters
        iterations: positive integer containing max iterations

    Returns:
        C: numpy.ndarray of shape (k, d) with centroid means
        clss: numpy.ndarray of shape (n,) with cluster indices
        or None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    n, d = X.shape

    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    C = np.random.uniform(low=min_vals, high=max_vals, size=(k, d))

    for _ in range(iterations):
        C_prev = np.copy(C)

        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(distances, axis=1)

        counts = np.bincount(clss, minlength=k)
        cluster_sums = np.zeros((k, d))
        np.add.at(cluster_sums, clss, X)

        mask = counts > 0
        C[mask] = cluster_sums[mask] / counts[mask, np.newaxis]

        empty = np.where(counts == 0)[0]
        if len(empty) > 0:
            C[empty] = np.random.uniform(
                low=min_vals, high=max_vals,
                size=(len(empty), d)
            )

        if np.array_equal(C, C_prev):
            break

    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    clss = np.argmin(distances, axis=1)

    return C, clss
