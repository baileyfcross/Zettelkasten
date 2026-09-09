2026-09-08 22:09

Status: #baby

Tags: [[Azure SignalR Service Applications]]

# Azure SignalR Service

Azure SignalR Service provides a managed connection layer for SignalR applications hosted in Azure. The application keeps its hub and client programming model while the service handles the infrastructure needed to maintain and scale many persistent client connections.

The book's ASP.NET Core 3 chat registers Azure SignalR after `AddSignalR`, maps a hub route, and supplies the Azure connection information through application settings. This separates real-time connection management from the chat-specific messages defined by the application.

# References

[[c8andnetcore30projectsusingazure.pdf]]
