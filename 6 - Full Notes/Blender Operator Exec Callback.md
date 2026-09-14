2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Exec Callback

An operator's `exec` callback performs the actual non-modal action. Blender passes the current [[Blender bContext Structure]] and [[Blender Operator Instance Structure]], giving the function access to active application state and the operation's RNA-backed settings.

The callback can retrieve values through [[Blender Operator RNA Properties]], call editor services, and delegate lower-level changes to the [[Blender BKE API]]. It returns an operator status such as finished so the handler system knows how to continue processing the event.

# References

[[coreblenderdevelopment.pdf]]

