2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon Data Firehose

Amazon Data Firehose is a managed delivery service that buffers streaming records and writes them to destinations such as Amazon S3, Amazon Redshift, and Amazon OpenSearch Service. It can transform records, compress output, and adapt delivery capacity without exposing a shard-management model to the user.

Firehose emphasizes reliable delivery into an analytics destination rather than retaining a stream for many independently managed consumers. [[Amazon Kinesis Data Streams]] is a better fit when applications need direct, repeatable consumption of ordered records.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
