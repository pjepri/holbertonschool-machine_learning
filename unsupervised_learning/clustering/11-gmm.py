#!/usr/bin/env python3
"""GMM using sklearn"""
import sklearn.mixture


def gmm(X, k):
    """
    Calculates a GMM from a dataset

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: number of clusters

    Returns:
        pi: numpy.ndarray of shape (k,) with cluster priors
        m: numpy.ndarray of shape (k, d) with centroid means
        S: numpy.ndarray of shape (k, d, d) with covariance matrices
        clss: numpy.ndarray of shape (n,) with cluster indices
        bic: the BIC value for the model
    """
    gmm_model = sklearn.mixture.GaussianMixture(n_components=k)
    gmm_model.fit(X)

    pi = gmm_model.weights_
    m = gmm_model.means_
    S = gmm_model.covariances_
    clss = gmm_model.predict(X)
    bic = gmm_model.bic(X)

    return pi, m, S, clss, bic
