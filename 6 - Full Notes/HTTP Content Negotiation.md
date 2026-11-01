2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# HTTP Content Negotiation

HTTP content negotiation lets a client state which representation media types it can accept and lets the server select a supported response format. The same resource may consequently be represented as JSON, XML, or another agreed form without receiving a different conceptual identity.

The book uses the `Accept` header both for ordinary format selection and for media-type versioning. A server should describe the selected type in its response and return a clear failure when it cannot produce any representation acceptable to the client.

# References

[[masteringrestapis.epub]]
