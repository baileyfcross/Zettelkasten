2026-09-15 23:23

Status: #baby

Tags: [[R Spatial Data Structures]]

# RasterStack

A `RasterStack` is a collection of raster layers that share compatible extent and resolution but may remain separate data sources. It provides one object for selecting, plotting, and calculating across variables or times. A `RasterBrick` stores a truly multilayer raster more compactly and can be more efficient, whereas a stack is flexible for combining files. A time index can turn either representation into a [[Time-Indexed Raster Stack]].

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
