2026-09-16 00:09

Status: #baby

Tags: [[R Programming Environment]]

# R Package Namespace

An R package namespace identifies which package supplies a function or object. The `package::function` notation calls an exported function without attaching the whole package and makes name conflicts visible in code.

Explicit namespaces are particularly useful in reusable scripts and functions where several packages may export similarly named operations.

The triple-colon form can reach an internal package object that was not exported, whereas the double-colon form is limited to the public namespace. Depending on internal objects couples code to implementation details and is therefore less stable than using an exported interface.

# References

[[essentialsofdatascience.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
