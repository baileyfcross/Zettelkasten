2026-09-26 22:56

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Adapter Pattern

The Adapter pattern places a translating object between a client and an incompatible interface. The client keeps using the contract it expects, while the adapter converts those calls and values into the form supplied by the existing component.

This preserves both sides from invasive changes and permits a different adapter for another implementation. The pattern is most useful when the mismatch is stable and translation is clearer than forcing either component to adopt the other's interface.

The current source distinguishes the expected client interface from the existing target interface and assigns their translation to the adapter. This is especially valuable when the target is a library that cannot be changed or the client has other users that make rewriting its contract unsafe.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

