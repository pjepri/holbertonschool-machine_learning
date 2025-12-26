#!/usr/bin/env python3
"""EM algorithm with GMM"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    Performs the expectation maximization with a GMM

    Args:
        X: numpy.ndarray of shape (n, d) containing the data set
        k: positive integer containing the number of clusters
        iterations: positive integer containing max iterations
        tol: non-negative float indicating tolerance of log likelihood
        verbose: boolean indicating whether to print in progress

    Returns:
        pi: numpy.ndarray of shape (k,) with priors
        m: numpy.ndarray of shape (k, d) with centroid means
        S: numpy.ndarray of shape (k, d, d) with covariance matrices
        g: numpy.ndarray of shape (k, n) with probabilities
        l: the log likelihood of the model
        or None, None, None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None, None
    if not isinstance(tol, (int, float)) or tol < 0:
        return None, None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    if pi is None:
        return None, None, None, None, None

    prev_ll = 0
    g, ll = None, None

    for i in range(iterations):
        g, ll = expectation(X, pi, m, S)
        if g is None:
            return None, None, None, None, None

        if verbose and i % 10 == 0:
            print("Log Likelihood after {} iterations: {}".format(
                i, round(ll, 5)))

        if abs(ll - prev_ll) <= tol:
            break

        prev_ll = ll

        pi, m, S = maximization(X, g)
        if pi is None:
            return None, None, None, None, None

    # Print final iteration if not already printed
    if verbose and i % 10 != 0:
        print("Log Likelihood after {} iterations: {}".format(
            i, round(ll, 5)))

    # Final E-step to ensure g and ll match final pi, m, S
    g, ll = expectation(X, pi, m, S)

    return pi, m, S, g, ll
