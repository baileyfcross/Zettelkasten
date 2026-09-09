2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]] [[Cloud Integration and Messaging]]

# Broadcast Message

A broadcast message is a real-time event sent to multiple connected clients. Server code uses the hub context to name the event and provide a payload, and every intended recipient with a matching handler can react to it.

Broadcasting is appropriate when a change should be visible broadly, such as a newly added answer. More selective delivery is needed when data or authorization differs among recipients.

In message-oriented integration, a broadcast message is published under a topic so interested receivers can obtain it without the sender addressing each one individually. This contrasts with [[Point-to-Point Messaging]] and requires consistent topic and access rules.

# References

[[aspnetcore3andreact.pdf]]

[[cloudcomputing_mit.epub]]
