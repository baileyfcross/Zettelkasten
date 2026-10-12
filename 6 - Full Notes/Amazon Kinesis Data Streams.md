2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon Kinesis Data Streams

Amazon Kinesis Data Streams ingests ordered records from continuously producing sources and retains them for real-time consumers. A partition key assigns records to shards, preserving order within each shard while distributing load across the stream.

Multiple consumers can independently process the same retained data for monitoring, analytics, or application reactions. The producer and consumer layers scale separately, but shard capacity and key distribution must be chosen to avoid uneven traffic concentration.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
