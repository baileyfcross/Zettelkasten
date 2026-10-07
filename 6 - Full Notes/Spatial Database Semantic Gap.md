2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Spatial Database Semantic Gap

The spatial database semantic gap is the mismatch between geographic concepts and the simple numbers, strings, tables, and operations of a conventional relational database. A land parcel is naturally a polygon with implicit relations such as adjacency and distance, but a nonspatial schema may fragment it into many rows and require cumbersome joins to reconstruct one spatial question.

User-defined [[Spatial Data Types]] and operations close the gap by letting database expressions match the problem's own concepts. This improves clarity as well as speed: the system can recognize an overlap or nearest-neighbor request and choose specialized algorithms instead of treating geometry as unrelated scalar fields.

# References

[[spatialcomputing.epub]]

