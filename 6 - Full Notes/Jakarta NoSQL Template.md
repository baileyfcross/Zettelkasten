2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta NoSQL Template

The Jakarta NoSQL Template is a higher-level data-access abstraction for inserting, finding, deleting, and querying mapped objects without exposing each database's low-level interaction details. It supplies common CRUD operations and a fluent query form, and dot notation can navigate into embedded object fields.

NoSQL categories do not all support the same operations: key-value stores may be limited to key access, document stores usually support richer filtering, and column-family behavior depends on the implementation. When an operation is unavailable, Jakarta NoSQL can report an UnsupportedOperationException, so the uniform API does not erase the underlying store's capabilities.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
