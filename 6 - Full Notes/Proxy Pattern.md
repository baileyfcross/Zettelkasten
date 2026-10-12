2026-09-26 22:56

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Proxy Pattern

The Proxy pattern places a stand-in object in front of another object and preserves a compatible access surface. The proxy controls when or how the real subject is reached, such as enforcing authorization, delaying an expensive operation, or isolating a third-party component.

Unlike an [[Adapter Pattern|adapter]], a proxy normally preserves the subject's conceptual interface rather than translating to a different one. Its added control should remain visible enough that callers understand latency, security, or lifetime effects.

Its proxy example places a representative object in front of another object to control access or add behavior without changing the caller's interface, a structure useful for remote, protected, or deferred interactions.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onobject-orientedprogrammingwithc.pdf]]
