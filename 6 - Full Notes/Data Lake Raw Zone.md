2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Lake Architecture and Governance]]

# Data Lake Raw Zone

The raw zone preserves incoming data in its original form before transformation. Keeping an immutable source copy supports replay, audit, and new processing methods when downstream logic changes. Access is normally narrow because raw records may contain sensitive or malformed content. Retention, encryption, source identity, ingestion time, and integrity metadata must be defined so “raw” means traceable original input rather than ungoverned storage.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

