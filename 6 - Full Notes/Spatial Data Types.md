2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Spatial Data Types

Spatial data types represent geographic forms as first-class database values. Points model discrete locations, line strings model routes or centerlines, polygons model bounded areas, and rasters model fields as cell grids. Operations such as distance, area, inside, and overlap then act on those forms directly.

Without these types, a programmer may have to distribute one polygon's points, edges, and connections across several ordinary tables and reconstruct its meaning for every query. Standardized geometry types narrow that [[Spatial Database Semantic Gap]] and let different applications reuse the same spatial operations.

# References

[[spatialcomputing.epub]]

