2026-11-08 16:45

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Change Data Capture Changefeed

A change data capture changefeed turns committed database changes into an ordered stream that can be delivered to sinks such as a webhook, Kafka, object storage, or cloud messaging. Downstream services can update specialized views without the writing service calling each consumer directly.

Because the feed originates from the database log, it can preserve changes that would be lost by an in-memory after-save callback. The sink and consumer still need checkpointing, retry, duplicate handling, schema evolution, and a policy for failures. CDC enables eventual consistency between stores; it does not make the remote update part of the original transaction.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
