2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Modal Operator Lifecycle

A modal Blender operator remains active while multiple events arrive, much like an ongoing dialog or interactive tool. Invocation establishes the operation, a modal callback processes later events, checks may revise properties, and cancellation or completion ends the interaction.

The [[Blender Operator Instance Structure]] retains the state needed between callbacks, and a modal key map can interpret input specifically for that operation. This contrasts with a [[Blender Non-Modal Operator]], whose [[Blender Operator Exec Callback]] performs the complete action in one call.

# References

[[coreblenderdevelopment.pdf]]

