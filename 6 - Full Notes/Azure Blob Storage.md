2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Azure Blob Storage

Azure Blob Storage stores file-like binary objects inside containers. The photo-storage service uses it to preserve images detected on a local computer by uploading each file stream to a named block blob.

Blob storage is managed independently from the local directory, so the application compares names and performs asynchronous upload or rename operations through the storage client. Durability and access cost depend on the account's tier and redundancy configuration.

The Azure data architecture map uses Blob Storage and Data Lake Storage as durable landing and raw-data layers. Objects can preserve source fidelity before downstream transformation, while lifecycle tiers, redundancy, namespace design, identity-based access, encryption, and immutability policies tune cost and governance. Treating raw storage as an architectural layer also makes replay possible when processing logic changes, provided retention and lineage are maintained.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
