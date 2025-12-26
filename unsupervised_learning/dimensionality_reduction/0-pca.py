#!/usr/bin/env python3
"""PCA dimensionality reduction module"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where:
            n is the number of data points
            d is the number of dimensions in each point
            all dimensions have a mean of 0 across all data points
        var: fraction of the variance that the PCA transformation
             should maintain

    Returns:
        W: numpy.ndarray of shape (d, nd) where nd is the new dimensionality
           the weights matrix that maintains var fraction of X's original
           variance
    """
    # Perform SVD on the centered data
    U, S, Vt = np.linalg.svd(X, full_matrices=False)

    # Variance explained by each component is proportional to S^2
    variance = S ** 2
    total_variance = np.sum(variance)

    # Calculate cumulative variance ratio
    cumulative_ratio = np.cumsum(variance) / total_variance

    # Find the number of components to maintain at least var variance
    # We need the smallest nd such that cumulative_ratio >= var
    nd = np.searchsorted(cumulative_ratio, var) + 1

    # Ensure we don't exceed the number of components
    nd = min(nd, len(S))

    # W is the first nd principal components
    W = Vt[:nd].T

    return W
