2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Azure Blob Storage

Azure Blob Storage stores file-like binary objects inside containers. The photo-storage service uses it to preserve images detected on a local computer by uploading each file stream to a named block blob.

Blob storage is managed independently from the local directory, so the application compares names and performs asynchronous upload or rename operations through the storage client. Durability and access cost depend on the account's tier and redundancy configuration.

# References

[[c8andnetcore30projectsusingazure.pdf]]
