2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Broadcast Message

A broadcast message is a real-time event sent to multiple connected clients. Server code uses the hub context to name the event and provide a payload, and every intended recipient with a matching handler can react to it.

Broadcasting is appropriate when a change should be visible broadly, such as a newly added answer. More selective delivery is needed when data or authorization differs among recipients.

# References

[[aspnetcore3andreact.pdf]]
