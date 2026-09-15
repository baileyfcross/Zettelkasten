2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# Dummy Clustering Algorithm Example

DummyAlgorithm demonstrates the minimum subclass contract without implementing a meaningful clustering method. It validates a named cluster-count parameter, fills an internal membership vector, and publishes that vector with an additional message.

The example shows how client code supplies a dataset and type-erased parameter, calls clusterize, and retrieves typed results. Its simplicity isolates framework mechanics from mathematical complexity.

# References

[[dataclusteringincplusplus.pdf]]

