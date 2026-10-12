2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Global Interpreter Lock

The CPython global interpreter lock coordinates access to shared Python objects when more than one thread could interact with the embedded interpreter. Blender must use the appropriate CPython lock-management functions so two execution paths do not update the same object simultaneously.

This concern sits beside the [[Blender Python Interpreter Lifecycle]] rather than changing the public script interface. Reference counting and locking together protect objects created by [[Blender CPython Extension Type]] implementations while native Blender subsystems continue to run around them.

# References

[[coreblenderdevelopment.pdf]]

