2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Design Patterns]]

# Pure Virtual Extension Point

A pure virtual extension point declares a required operation without a base implementation. Concrete clustering classes must supply the operation before they can be instantiated, as linkage subclasses implement distance updates and algorithms implement their computation and result transfer.

The extension point isolates genuine variation while the surrounding base class preserves shared behavior. Too many hooks expose unstable internals, whereas too few force subclasses to duplicate the control flow.

# References

[[dataclusteringincplusplus.pdf]]

