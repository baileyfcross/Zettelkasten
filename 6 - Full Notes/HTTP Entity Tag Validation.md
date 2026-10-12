2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# HTTP Entity Tag Validation

HTTP entity tag validation associates a response representation with an `ETag`. On a later request, the client sends the known tag in a conditional header, and the server can return `304 Not Modified` instead of retransmitting an unchanged body.

This preserves freshness more accurately than relying only on a local age threshold. The tag validates a particular representation, so client and server must keep cache keys and request variants aligned.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
