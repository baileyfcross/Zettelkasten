2026-09-15 23:23

Status: #baby

Tags: [[R Spatiotemporal Data Structures]]

# Time-Indexed Raster Stack

A time-indexed raster stack attaches a temporal coordinate to every layer of a `RasterStack` or `RasterBrick`. In R, `setZ` records the index and `getZ` retrieves it, allowing operations such as `zApply` to group layers through time. The structure treats aligned rasters as successive snapshots of one [[Space-Time Raster]] rather than unrelated files, while retaining their shared extent and resolution.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
