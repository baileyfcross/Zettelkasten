2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Spatial Nearest Neighbor Query

A spatial nearest-neighbor query identifies the stored object or objects closest to a specified location or geometry. A navigation service can use it to find the nearest park or business, while a planning system can locate the closest facility to a parcel.

Distance must be evaluated in an appropriate coordinate model, and a linear scan becomes expensive as the collection grows. A [[Spatial Index]] supplies promising candidates and lower bounds that let the database avoid measuring every object before returning the nearest result.

# References

[[spatialcomputing.epub]]

