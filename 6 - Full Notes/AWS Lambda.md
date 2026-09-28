2026-09-27 18:58

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# AWS Lambda

AWS Lambda runs function code in response to events without the customer provisioning or managing servers. Billing follows invocations and execution resources, while the platform creates and scales execution environments as demand arrives.

Functions work well for event-driven, bounded processing such as reacting to an S3 upload or schedule. Execution duration, statelessness, cold starts, permissions, retry behavior, and idempotency shape the design. Serverless removes server management, not application responsibility.

Lambda execution environments may be reused, so initialization outside the handler can reduce repeated setup cost, but durable application state must live elsewhere. Concurrency connects incoming demand to simultaneous execution environments; reserved or provisioned concurrency can protect capacity or reduce cold-start latency when those guarantees justify their cost.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
