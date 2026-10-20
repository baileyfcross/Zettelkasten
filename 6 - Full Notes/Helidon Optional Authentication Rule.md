2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Optional Authentication Rule

A Helidon path can mark authentication as optional even when its rule names an allowed role. In that mode, a missing identity does not cause the server to return an authentication challenge.

Optional authentication does not grant the named role to an anonymous caller. In the book's example, the path still remains forbidden because an administrator role is required; the difference is that failure is reported without asking the client to authenticate.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
