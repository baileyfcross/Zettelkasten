2026-09-08 22:09

Status: #baby

Tags: [[Azure SignalR Service Applications]]

# SignalR Client Handler

A SignalR client handler is a function registered under the name of a server-sent event. When the hub invokes that name, the client library passes the message arguments to the handler so it can update the page or application state.

Handler names form part of the live communication contract. The chat client registers separate handlers for incoming chat content and archive confirmation, keeping the presentation response aligned with the event's purpose.

# References

[[c8andnetcore30projectsusingazure.pdf]]
