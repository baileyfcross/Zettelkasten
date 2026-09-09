2026-09-08 22:09

Status: #baby

Tags: [[Azure SignalR Service Applications]]

# SignalR Hub Method

A SignalR hub method is a public server operation that a connected client can invoke through the hub connection. It receives the client's supplied arguments, performs the relevant application work, and can call one or more client methods in response.

The book's send method returns the task produced by broadcasting `UpdateChat`, while its archive method writes a transcript and then broadcasts `Archived`. Returning the asynchronous operation lets completion and failures remain part of the hub call.

# References

[[c8andnetcore30projectsusingazure.pdf]]
