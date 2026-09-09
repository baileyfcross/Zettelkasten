2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Block Blob

A block blob is the Azure blob type used by the project to hold an uploaded image file. The client can obtain a reference before the object exists and then create or replace its content by uploading a stream.

Treating the blob reference as a remote file handle separates naming from transfer. The application still needs to handle invalid configuration, network failures, and the possibility that a local file changes while it is being processed.

# References

[[c8andnetcore30projectsusingazure.pdf]]
