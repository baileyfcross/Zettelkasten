2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Hub Connection

A hub connection is the client-side object that represents an active SignalR relationship with a hub endpoint. It is configured with the server URL, registers handlers for server messages, and is then started asynchronously.

The connection belongs to the lifetime of the UI behavior that consumes it. Setup and cleanup therefore need to be paired so navigation and rerendering do not create duplicate subscriptions.

# References

[[aspnetcore3andreact.pdf]]
