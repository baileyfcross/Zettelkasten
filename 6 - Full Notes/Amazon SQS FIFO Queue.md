2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon SQS FIFO Queue

An Amazon SQS FIFO queue preserves message order within a message group and supports exactly-once processing semantics through deduplication. Producers supply grouping and deduplication information so SQS can sequence related work and suppress repeated submissions within the deduplication interval.

These guarantees trade some flexibility and throughput for stricter behavior. FIFO is appropriate when order affects correctness, while an [[Amazon SQS Standard Queue]] is generally preferred for independent tasks that can be processed in any order.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
