2026-09-08 22:09

Status: #baby

Tags: [[WebAssembly and Blazor Applications]]

# Server-Side Blazor

Server-side Blazor runs component C# code on the server and transmits interface updates to the browser through SignalR. It uses the Blazor component model without running that application code as WebAssembly on the client.

The source identifies server-side Blazor as the flavor released with .NET Core 3. Its architecture trades the client's runtime download for a continuing real-time connection to server-hosted state and execution.

# References

[[c8andnetcore30projectsusingazure.pdf]]
