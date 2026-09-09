2026-09-09 00:00

Status: #baby

Tags: [[Cloud Integration and Messaging]]

# Reliable Message Delivery

Reliable message delivery uses an acknowledgment or handshake to give the sender evidence that a message or ordered block of messages reached the receiver. If acknowledgment does not arrive, the system can retain or resend the work according to its policy.

Reliability reduces silent loss but does not by itself guarantee one-time processing. Retries can produce duplicate delivery unless message identity and consumer behavior make repeated work safe.

# References

[[cloudcomputing_mit.epub]]
