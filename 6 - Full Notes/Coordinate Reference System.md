2026-09-15 23:23

Status: #baby

Tags: [[R Spatial Data Structures]] [[GIS and Cartographic Reasoning]]

# Coordinate Reference System

A coordinate reference system defines how numeric coordinates correspond to locations on the Earth. It includes a datum and may include a projection that transforms the curved surface into planar coordinates. Spatial layers must use compatible systems before their geometries can be overlaid correctly. [[Spatial Data Reprojection]] changes coordinate values between systems; merely relabeling coordinates does not perform that transformation.

Different datums model Earth's shape and reference frame differently, so an identical latitude-and-longitude pair can identify points separated by a meaningful distance. A GIS must retain and transform the coordinate reference with the values, and the chosen projection must match the distance, direction, area, or shape relationships the analysis needs to preserve.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
[[spatialcomputing.epub]]
