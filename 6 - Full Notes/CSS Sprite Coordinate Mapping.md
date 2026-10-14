2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# CSS Sprite Coordinate Mapping

A CSS sprite map records the position and dimensions of each packed image within a shared raster. CSS background position offsets move the desired rectangle under an element’s visible box.

Automated packing and generated styles reduce coordinate errors. Padding may be needed to prevent neighboring pixels from bleeding during scaling or high-density rendering. Any repack can change many offsets, so the map and sprite should be generated as one versioned artifact.

# References

[[highperformanceimages.pdf]]
