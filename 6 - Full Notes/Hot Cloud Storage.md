2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Hot Cloud Storage

Hot cloud storage is optimized for data that is accessed frequently. Its storage cost is higher than a colder tier, while reading and writing the data is comparatively less expensive.

The photo project uses hot storage during development and testing because files are repeatedly exercised. Tier selection should follow the expected access pattern rather than the file type alone.

# References

[[c8andnetcore30projectsusingazure.pdf]]
