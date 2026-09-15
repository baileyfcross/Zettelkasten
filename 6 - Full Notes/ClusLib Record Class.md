2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# ClusLib Record Class

Record inherits a typed container of AttrValue objects and adds a shared schema, a label value, and an identifier value. The schema describes every component and is shared with other records in the same dataset.

Container methods provide indexed value access, while record methods expose identity and optional class information. Copying a record can share its immutable schema rather than duplicating the entire attribute-description graph.

# References

[[dataclusteringincplusplus.pdf]]

