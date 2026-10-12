2026-09-27 20:01

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Access Point

An Amazon S3 Access Point gives a bucket an additional named endpoint with its own access policy and optional VPC restriction. Teams or applications can receive separate entry points to the same shared bucket, making permissions easier to express than one expanding bucket policy. Access points do not copy the objects; they create distinct governed paths whose policies must still align with the bucket and account-level public-access controls.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

