2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Spatial Join

A spatial join pairs records from two spatial data sets when their geometries satisfy a relation such as overlap, containment, adjacency, or proximity. Joining lake polygons with adjacent land parcels, for example, produces parcel–lake pairs even when the tables share no ordinary key.

The geographic predicate functions as the join condition. Because comparing every feature in one set with every feature in the other is costly, a database can combine indexes with a [[Plane Sweep Algorithm]] or another geometric method to reduce the candidate pairs before exact evaluation.

# References

[[spatialcomputing.epub]]

