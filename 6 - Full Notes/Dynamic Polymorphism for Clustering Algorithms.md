2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Object Model]]

# Dynamic Polymorphism for Clustering Algorithms

Dynamic polymorphism lets a base-class pointer or reference invoke an overridden operation selected from the object's runtime type. ClusLib uses virtual functions so a caller can execute distinct algorithms, distance measures, adapters, and tree visitors through shared interfaces.

The mechanism separates the client from concrete class names and supports replacement at runtime. It also requires virtual destructors and clear ownership because deleting a derived object through an incomplete base interface must still release the full object correctly.

# References

[[dataclusteringincplusplus.pdf]]

