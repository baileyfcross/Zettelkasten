2026-09-08 22:09

Status: #baby

Tags: [[Azure SignalR Service Applications]]

# SignalR Service Registration

SignalR service registration adds the framework's real-time services to ASP.NET Core dependency injection and, in the book's 2019 project, chains the Azure SignalR integration onto that registration. The middleware configuration then maps the chat hub to a public route.

Registration and route mapping solve different parts of startup: one makes services available to application code, and the other places the hub in the HTTP pipeline. Static and default-file middleware can serve the browser client alongside the live endpoint.

# References

[[c8andnetcore30projectsusingazure.pdf]]
