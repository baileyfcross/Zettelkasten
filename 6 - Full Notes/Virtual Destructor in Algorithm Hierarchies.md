2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Object Model]]

# Virtual Destructor in Algorithm Hierarchies

A virtual destructor ensures that deleting an object through a base pointer invokes the derived destructor before the base destructor. ClusLib gives base classes such as Algorithm, Distance, Cluster, Schema, and Node virtual destructors when they participate in runtime polymorphism.

Without this rule, derived resources may not be released and behavior is undefined. Declaring the destructor virtual documents that the class is intended as a polymorphic boundary even when the base itself owns little state.

# References

[[dataclusteringincplusplus.pdf]]

