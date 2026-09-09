2026-09-08 22:09

Status: #baby

Tags: [[Azure SignalR Service Applications]]

# SignalR Server Push

SignalR server push lets server-side code invoke named functions on connected clients without waiting for each client to poll for a change. The chat hub broadcasts a sender and message to every client as soon as its send method is called.

Push communication is useful for events whose value depends on timeliness, such as a new chat message or archive notification. The client must register a handler with the same event name and compatible arguments or the message cannot update its interface.

# References

[[c8andnetcore30projectsusingazure.pdf]]
