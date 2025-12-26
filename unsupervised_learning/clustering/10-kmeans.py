#!/usr/bin/env python3
"""K-means using sklearn"""
import sklearn.cluster


def kmeans(X, k):
    """
    Performs K-means on a dataset

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        k: number of clusters

    Returns:
        C: numpy.ndarray of shape (k, d) with centroid means
        clss: numpy.ndarray of shape (n,) with cluster indices
    """
    kmeans_model = sklearn.cluster.KMeans(n_clusters=k)
    kmeans_model.fit(X)

    C = kmeans_model.cluster_centers_
    clss = kmeans_model.labels_

    return C, clss
