2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Object Model]]

# Clustering Library Abstract Base Class

An abstract base class defines the stable operations shared by a family of clustering components while leaving at least one operation pure virtual. Clients program against the base interface, and derived classes provide the algorithm- or data-specific behavior.

The abstraction should contain only genuinely common responsibilities. Moving every possible option into the base class produces coupling, whereas focused extension points allow new algorithms, distances, adapters, or visitors to enter the framework independently.

# References

[[dataclusteringincplusplus.pdf]]

