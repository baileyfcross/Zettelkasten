2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Bindable Event

A BindableEvent provides event-based communication between scripts on the same side of the Roblox client-server boundary. One script fires the event and any connected listeners react without the sender calling them directly.

This decouples the producer of a gameplay occurrence from its consumers. A scoring script, interface controller, and effects script can respond independently to one local signal. Bindable events do not cross the network; communication between a client and server instead uses [[Roblox RemoteEvent]] or [[Roblox RemoteFunction]].

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

