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
    # Validate inputs
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    n, d = X.shape

    # Initialize centroids using uniform distribution
    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)
    C = np.random.uniform(low=min_vals, high=max_vals, size=(k, d))

    # K-means main loop (1st loop)
    for _ in range(iterations):
        # Copy centroids to check for convergence
        C_prev = np.copy(C)

        # Compute distances from each point to each centroid
        # X[:, np.newaxis] has shape (n, 1, d), C has shape (k, d)
        # Broadcasting gives (n, k, d), norm reduces to (n, k)
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)

        # Assign each point to nearest centroid
        clss = np.argmin(distances, axis=1)

        # Update centroids (2nd loop)
        for j in range(k):
            # Get points assigned to cluster j
            mask = clss == j
            if np.sum(mask) > 0:
                C[j] = np.mean(X[mask], axis=0)

        # Handle empty clusters - reinitialize
        empty_clusters = np.where(np.bincount(clss, minlength=k) == 0)[0]
        if len(empty_clusters) > 0:
            C[empty_clusters] = np.random.uniform(
                low=min_vals, high=max_vals,
                size=(len(empty_clusters), d)
            )

        # Check for convergence (no change in centroids)
        if np.array_equal(C, C_prev):
            break

    # Final assignment after convergence
    distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
    clss = np.argmin(distances, axis=1)

    return C, clss
