2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Operator Callback Binding

An operator registration function fills a [[Blender Operator Type Structure]] with identity, description, flags, properties, and function pointers. For the icosphere example, the registration assigns a concrete execution function to `exec` and a context-checking function to `poll`.

This binding separates the persistent description of an operation from the code that performs it. A later user event retrieves the registered type, the [[Blender Operator Poll Method]] decides whether it is valid in the current context, and the execution callback changes Blender data.

# References

[[coreblenderdevelopment.pdf]]

