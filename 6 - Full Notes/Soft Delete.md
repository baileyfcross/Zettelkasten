2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# Soft Delete

Soft deletion marks a record as deleted instead of physically removing it from storage. Queries hide marked records from ordinary use while preserving data that may be required for recovery, audit, or related history.

The policy must be applied consistently to reads, updates, and uniqueness rules. A delete endpoint can keep the same public intent even though the repository performs a state transition rather than a database `DELETE` operation.

The EF Core chapter implements soft deletion with an `IsDeleted` property and a global query filter, making ordinary queries omit deleted rows while preserving the records for recovery or audit behavior.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
