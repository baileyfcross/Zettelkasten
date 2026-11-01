2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API Media Type Versioning

API media type versioning encodes a contract version in the requested representation type, commonly through an `Accept` value such as a vendor-specific versioned JSON media type. The resource URI remains stable while content negotiation selects its versioned representation.

This aligns version choice with representation semantics, but the media-type vocabulary and fallback behavior must be documented. The server must also emit an accurate response content type so the client can verify which contract it received.

# References

[[masteringrestapis.epub]]
