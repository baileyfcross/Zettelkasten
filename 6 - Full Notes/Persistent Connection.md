2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Persistent Connection

A persistent connection remains available across multiple messages instead of ending after one request-response exchange. SignalR manages this ongoing communication channel and chooses suitable transport behavior for the client and server environment.

Because the channel has a lifetime, connection state becomes part of application behavior. Startup, disconnection, retry, and cleanup must be considered alongside the messages themselves.

# References

[[aspnetcore3andreact.pdf]]
