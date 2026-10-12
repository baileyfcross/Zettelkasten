2026-10-04 16:30

Status: #baby

Tags: [[Roblox Multiplayer and Platform Operations]]

# Roblox RemoteFunction

A RemoteFunction performs a request across the Roblox client-server boundary and waits for the remote callback to return a value. This makes it suitable when the caller cannot proceed without a specific answer.

Waiting also creates risk: slow or failing remote work can stall the caller, and invoking a client from the server depends on that client responding. A [[Roblox RemoteEvent]] is safer for one-way notifications and many gameplay updates. Any client-to-server function arguments still require [[Roblox Server-Side Validation]] before the server uses them.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

