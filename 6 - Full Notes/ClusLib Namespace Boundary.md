2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Build and Testing]]

# ClusLib Namespace Boundary

The ClusLib namespace contains the library's public types, functions, and aliases so they do not collide with names from the standard library, Boost, or client programs. Users can qualify names explicitly or introduce selected using declarations in limited scopes.

An umbrella header can expose the library while the namespace preserves its boundary. Broad using directives in headers would leak names into clients, so namespace convenience belongs primarily in implementation or example files.

# References

[[dataclusteringincplusplus.pdf]]

