2026-09-09 00:00

Status: #baby

Tags: [[Cloud Integration and Messaging]]

# Message Correlation Identifier

A message correlation identifier labels messages that belong to the same task, conversation, sender, or group. A receiver can use it to collect related messages, preserve a sequence within a group, or match a response to the request that caused it.

Correlation lets independent messages retain business context without embedding transport assumptions in application logic. The identifier must remain unique within its intended scope and be propagated across every participating service.

# References

[[cloudcomputing_mit.epub]]
