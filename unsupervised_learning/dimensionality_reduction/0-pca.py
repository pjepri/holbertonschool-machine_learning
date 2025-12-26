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
    # X = U @ S @ Vt
    # The rows of Vt (columns of V) are the principal components
    U, S, Vt = np.linalg.svd(X, full_matrices=False)

    # Variance explained by each component is proportional to S^2
    variance = S ** 2
    total_variance = np.sum(variance)

    # Calculate cumulative variance ratio
    cumulative_variance_ratio = np.cumsum(variance) / total_variance

    # Find number of components needed to maintain var fraction
    # argmax returns the first index where condition is True
    nd = np.argmax(cumulative_variance_ratio >= var) + 1

    # W is the first nd principal components (columns of V = rows of Vt)
    # Shape: (d, nd)
    W = Vt[:nd].T

    return W

