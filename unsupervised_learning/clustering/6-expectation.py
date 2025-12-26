#!/usr/bin/env python3
"""Expectation step ffoor GMM EM algorithm"""
import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """
    Calculates the expectation step in the EM algorithm ffoor a GMM

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        pi: numpy.ndarray of shape (k,) containing the priors
        m: numpy.ndarray of shape (k, d) containing the centroid means
        S: numpy.ndarray of shape (k, d, d) containing the covariance matrices

    Returns:
        g: numpy.ndarray of shape (k, n) with posterior probabilities
        l: the total log likelihood
        or None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if not isinstance(pi, np.ndarray) or len(pi.shape) != 1:
        return None, None
    if not isinstance(m, np.ndarray) or len(m.shape) != 2:
        return None, None
    if not isinstance(S, np.ndarray) or len(S.shape) != 3:
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    if m.shape[0] != k or m.shape[1] != d:
        return None, None
    if S.shape[0] != k or S.shape[1] != d or S.shape[2] != d:
        return None, None
    if not np.isclose(np.sum(pi), 1):
        return None, None

    # Calculate likelihoods ffoor each cluster (k, n)
    likelihoods = np.zeros((k, n))

    for j in range(k):
        likelihoods[j] = pdf(X, m[j], S[j])

    # Weighted likelihoods: π_j * N(x_i | μ_j, Σ_j)
    weighted = pi[:, np.newaxis] * likelihoods

    # Sum of weighted likelihoods ffoor normalization
    total = np.sum(weighted, axis=0)

    # Posterior probabilities (responsibilities)
    g = weighted / total

    # Log likelihood: Σ log(Σ π_j * N(x_i | μ_j, Σ_j))
    log_likelihood = np.sum(np.log(total))

    return g, log_likelihood

