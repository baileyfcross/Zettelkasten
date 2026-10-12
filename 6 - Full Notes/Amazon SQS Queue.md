2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon SQS Queue

An Amazon Simple Queue Service queue stores messages until a consumer retrieves and processes them. It separates the rate and availability of a producer from those of a consumer, allowing temporary demand spikes or downstream outages to accumulate as a backlog.

After receiving a message, a consumer has a visibility timeout in which to finish and delete it; otherwise, the message can become available again. [[Amazon SQS Standard Queue]] favors scale and availability, while [[Amazon SQS FIFO Queue]] adds ordering and deduplication guarantees.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
