2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# ClusLib Algorithm Base Class

Algorithm is the polymorphic base for clustering methods. It owns Arguments and mutable Results, retains the dataset used during computation, exposes configuration and result access, and defines the public clusterize operation.

A virtual destructor and virtual lifecycle methods allow concrete algorithms to specialize behavior safely. The base class centralizes the contract that every method accepts inputs, performs clustering, and publishes results.

# References

[[dataclusteringincplusplus.pdf]]

