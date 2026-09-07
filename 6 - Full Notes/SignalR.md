2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# SignalR

SignalR is an ASP.NET Core library for real-time communication between server code and connected clients. Unlike a REST exchange initiated only by the client, it lets the server send a message when an event occurs.

A server exposes a hub and a React client creates a hub connection with named message handlers. This supplements rather than replaces REST: commands and resource retrieval can remain HTTP operations while notifications travel over the live connection.

# References

[[aspnetcore3andreact.pdf]]
