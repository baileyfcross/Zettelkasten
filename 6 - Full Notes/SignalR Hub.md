2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]] [[Azure SignalR Service Applications]]

# SignalR Hub

A SignalR hub is the server-side endpoint through which clients and the application exchange named real-time messages. ASP.NET Core maps the hub to a route and makes its client communication interface available through dependency injection.

Application code can use the hub context to publish after a successful state change. Keeping the database write authoritative prevents a notification from claiming that an operation succeeded before it actually did.

In the chat project, a hub subclass exposes methods whose calls end in `Clients.All.SendAsync`, causing every connected client to invoke a named handler with the supplied values. The hub route is mapped during application startup after SignalR and the Azure SignalR integration are registered.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andreact.pdf]]
