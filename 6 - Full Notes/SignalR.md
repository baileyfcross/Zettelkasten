2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]] [[Azure SignalR Service Applications]]

# SignalR

SignalR is an ASP.NET Core library for real-time communication between server code and connected clients. Unlike a REST exchange initiated only by the client, it lets the server send a message when an event occurs.

A server exposes a hub and a React client creates a hub connection with named message handlers. This supplements rather than replaces REST: commands and resource retrieval can remain HTTP operations while notifications travel over the live connection.

The Azure chat project separates SignalR's programming model from its hosting infrastructure. The application still defines a hub and named client callbacks, while Azure SignalR Service manages the scalable connection layer used to broadcast chat and archive notifications.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andreact.pdf]]
