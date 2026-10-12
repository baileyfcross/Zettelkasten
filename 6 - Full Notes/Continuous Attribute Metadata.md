2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# Continuous Attribute Metadata

CAttrInfo interprets an AttrValue as a continuous numeric quantity. It supplies conversion, access, equality, and component-distance behavior appropriate to real-valued attributes.

Keeping numeric operations in metadata prevents dataset and distance code from scattering variant casts. A schema can ask whether an attribute supports continuous access before an algorithm assumes numeric input.

# References

[[dataclusteringincplusplus.pdf]]

