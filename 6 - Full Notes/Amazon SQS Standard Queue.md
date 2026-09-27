2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon SQS Standard Queue

An Amazon SQS standard queue provides highly scalable message storage with at-least-once delivery and best-effort ordering. A message can occasionally be delivered more than once or arrive out of sequence, so consumers should be idempotent and tolerate reordering.

This queue type is appropriate when throughput and loose coupling matter more than strict order. Workloads that require messages to be processed in sequence and without duplicate delivery attempts should consider an [[Amazon SQS FIFO Queue]].

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
