2026-10-04 16:30

Status: #baby

Tags: [[Roblox Multiplayer and Platform Operations]]

# Roblox RemoteEvent

A RemoteEvent sends an asynchronous message across the Roblox client-server boundary. A client can fire the server, the server can fire one client, or the server can broadcast to all clients without waiting for a returned value.

Events fit notifications and requests whose sender can continue immediately, such as reporting input, announcing an effect, or distributing a state change. Payloads should be small and purposeful, and the server must validate client-supplied values. When the caller genuinely needs a reply before continuing, [[Roblox RemoteFunction]] provides a synchronous request-response pattern.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

