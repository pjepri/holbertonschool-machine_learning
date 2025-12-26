#!/usr/bin/env python3
"""Maximization step for GMM EM algorithm"""
import numpy as np


def maximization(X, g):
    """
    Calculates the maximization step in the EM algorithm for a GMM

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        g: numpy.ndarray of shape (k, n) containing the posterior probabilities

    Returns:
        pi: numpy.ndarray of shape (k,) with updated priors
        m: numpy.ndarray of shape (k, d) with updated centroid means
        S: numpy.ndarray of shape (k, d, d) with updated covariance matrices
        or None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None

    n, d = X.shape
    k = g.shape[0]

    if g.shape[1] != n:
        return None, None, None

    # Check that posterior probabilities sum to 1 for each point
    if not np.allclose(np.sum(g, axis=0), 1):
        return None, None, None

    # N_k = Σ_i γ(z_ik) - effective number of points in each cluster
    N_k = np.sum(g, axis=1)

    # Updated priors: π_k = N_k / N
    pi = N_k / n

    # Updated means: μ_k = (1/N_k) * Σ_i γ(z_ik) * x_i
    m = (g @ X) / N_k[:, np.newaxis]

    # Updated covariances
    S = np.zeros((k, d, d))
    for j in range(k):
        diff = X - m[j]
        S[j] = (diff.T @ (g[j][:, np.newaxis] * diff)) / N_k[j]

    return pi, m, S
