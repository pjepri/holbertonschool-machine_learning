#!/usr/bin/env python3
"""Calculate PDF of a Gaussian distribution"""
import numpy as np


def pdf(X, m, S):
    """
    Calculates the probability density function of a Gaussian distribution

    Args:
        X: numpy.ndarray of shape (n, d) containing data points
        m: numpy.ndarray of shape (d,) containing the mean
        S: numpy.ndarray of shape (d, d) containing the covariance

    Returns:
        P: numpy.ndarray of shape (n,) containing the PDF values
        or None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(m, np.ndarray) or len(m.shape) != 1:
        return None
    if not isinstance(S, np.ndarray) or len(S.shape) != 2:
        return None

    n, d = X.shape

    if m.shape[0] != d:
        return None
    if S.shape[0] != d or S.shape[1] != d:
        return None

    # Calculate determinant and inverse of covariance matrix
    det = np.linalg.det(S)
    S_inv = np.linalg.inv(S)

    # Normalization constant: (2π)^(d/2) * |Σ|^(1/2)
    norm = np.sqrt(((2 * np.pi) ** d) * det)

    # Difference from mean for all data points: (x - μ)
    diff = X - m

    # Quadratic form: (x - μ)^T * Σ^(-1) * (x - μ) for each point
    exponent = np.sum((diff @ S_inv) * diff, axis=1)

    # PDF values
    P = np.exp(-0.5 * exponent) / norm

    # Apply minimum value
    P = np.maximum(P, 1e-300)

    return P
