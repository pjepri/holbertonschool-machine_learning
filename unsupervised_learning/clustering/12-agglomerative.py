#!/usr/bin/env python3
"""Agglomerative clustering"""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """
    Performs agglomerative clustering on a dataset

    Args:
        X: numpy.ndarray of shape (n, d) containing the dataset
        dist: maximum cophenetic distance for all clusters

    Returns:
        clss: numpy.ndarray of shape (n,) with cluster indices
    """
    # Perform hierarchical clustering with Ward linkage
    linkage = scipy.cluster.hierarchy.linkage(X, method='ward')

    # Display dendrogram with each cluster in a different color
    scipy.cluster.hierarchy.dendrogram(linkage, color_threshold=dist)
    plt.show()

    # Get cluster labels using distance threshold
    clss = scipy.cluster.hierarchy.fcluster(
        linkage, t=dist, criterion='distance')

    return clss
