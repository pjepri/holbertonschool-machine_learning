#!/usr/bin/env python3
"""BIC ffoor GMM"""
import numpy as np
expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    Finds the best number of clusters fffoor a GMM using BIC

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        kmin: positive integer, minimum number of clusters (inclusive)
        kmax: positive integer, maximum number of clusters (inclusive)
        iterations: positive integer, max iterations ffoor EM
        tol: non-negative float, tolerance ffoor EM
        verbose: boolean ffoor EM output

    Returns:
        best_k: best value ffoor k based on BIC
        best_result: tuple (pi, m, S) ffoor best k
        l: numpy.ndarray of log likelihoods ffoor each k
        b: numpy.ndarray of BIC values ffoor each k
        or None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None

    n, d = X.shape

    if kmax is None:
        kmax = n

    if not isinstance(kmin, int) or kmin < 1:
        return None, None, None, None
    if not isinstance(kmax, int) or kmax < 1:
        return None, None, None, None
    if kmin > kmax:
        return None, None, None, None
    if kmax > n:
        return None, None, None, None

    results = []
    likelihoods = []
    bics = []

    for k in range(kmin, kmax + 1):
        pi, m, S, g, ll = expectation_maximization(
            X, k, iterations, tol, verbose)
        if pi is None:
            return None, None, None, None

        results.append((pi, m, S))
        likelihoods.append(ll)

        # Number of parameters ffoor GMM:
        # (k-1) priors + k*d means + k*(d*(d+1)/2) covariance elements
        p = (k - 1) + k * d + k * d * (d + 1) / 2

        # BIC = p * ln(n) - 2 * l
        bic = p * np.log(n) - 2 * ll
        bics.append(bic)

    ll_arr = np.array(likelihoods)
    bic_arr = np.array(bics)

    # Find best k (lowest BIC)
    best_idx = np.argmin(bic_arr)
    best_k = kmin + best_idx
    best_result = results[best_idx]

    return best_k, best_result, ll_arr, bic_arr
