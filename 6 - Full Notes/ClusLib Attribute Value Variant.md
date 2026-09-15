2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# ClusLib Attribute Value Variant

AttrValue stores an individual attribute as a Boost variant capable of holding the supported underlying value forms. The value object does not decide how a categorical code or continuous number should be interpreted; that responsibility belongs to attribute metadata.

A variant is more type-safe than an untagged union because retrieval checks the active type. Separating storage from interpretation lets records use one vector type across numeric, categorical, identifier, and label fields.

# References

[[dataclusteringincplusplus.pdf]]

