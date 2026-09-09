2026-09-09 00:00

Status: #baby

Tags: [[Cloud Integration and Messaging]]

# Transacted Message

A transacted message participates in an end-to-end transaction or business function. Delivery is considered complete only when the associated transaction commits rather than merely when the message arrives at a receiver.

This connects messaging success to a wider unit of work. The transaction boundary, rollback behavior, and participating systems must be defined so a transport acknowledgment is not mistaken for completed business processing.

# References

[[cloudcomputing_mit.epub]]
