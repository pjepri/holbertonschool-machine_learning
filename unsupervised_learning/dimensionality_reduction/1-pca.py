#!/usr/bin/env python3
"""PCA dimensionality reduction module v2"""
import numpy as np


def pca(X, ndim):
    """
    Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where:
            n is the number of data points
            d is the number of dimensions in each point
        ndim: the new dimensionality of the transformed X

    Returns:
        T: numpy.ndarray of shape (n, ndim) containing the transformed
           version of X
    """
    # Center the data by subtracting the mean
    X_centered = X - np.mean(X, axis=0)

    # Perform SVD on the centered data
    # X = U @ S @ Vt
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

    # W is the first ndim principal components (columns of V = rows of Vt)
    W = Vt[:ndim].T

    # Transform the data
    T = np.matmul(X_centered, W)

    return T
