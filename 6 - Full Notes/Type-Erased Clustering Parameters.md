2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# Type-Erased Clustering Parameters

Type-erased clustering parameters are stored as boost::any values under string keys. One Arguments object can therefore carry integers, real tolerances, matrices, messages, or other types required only by a particular algorithm.

The concrete setup hook restores the expected type with any_cast and validates the value. This extensibility trades compile-time checking for a runtime key-and-type contract.

# References

[[dataclusteringincplusplus.pdf]]

