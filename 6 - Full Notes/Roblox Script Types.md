2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Script Types

Roblox uses Script, LocalScript, and ModuleScript objects for different execution roles. A Script normally runs authoritative server logic, a LocalScript runs for an individual client in an allowed client context, and a ModuleScript returns reusable values or functions when required.

Correct placement matters because an otherwise valid script may never execute in the wrong container. The choice also establishes security and replication boundaries, especially in [[Roblox Client-Server Replication]]. Shared libraries belong in [[Roblox ModuleScript]], while server and client scripts should contain only the responsibilities appropriate to their side.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

