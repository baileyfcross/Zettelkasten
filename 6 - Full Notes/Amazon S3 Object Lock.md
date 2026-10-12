2026-09-27 20:01

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Object Lock

Amazon S3 Object Lock applies write-once, read-many retention to versioned objects so protected versions cannot be overwritten or deleted before their retention expires. Governance mode allows specially authorized overrides, while compliance mode prevents even privileged users from shortening the retention period. Legal holds preserve selected versions without a fixed expiry. Object Lock is useful for records and immutable logs, but retention settings require careful policy because they intentionally resist deletion.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

