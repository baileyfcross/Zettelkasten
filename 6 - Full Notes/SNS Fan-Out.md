2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# SNS Fan-Out

SNS fan-out publishes an event to one [[Amazon SNS Topic]] and delivers a separate copy to multiple subscribed consumers, often through individual SQS queues. Each consumer can then process the event at its own rate and retry independently.

The pattern avoids coupling a producer to every downstream service. A failed or slow consumer does not need to block the others, and a new consumer can be added by subscribing another endpoint without changing the publisher.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
