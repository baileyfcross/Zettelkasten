2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# HTTP DELETE

HTTP DELETE requests removal of the resource identified by the target URI. The controller resolves the identifier, applies any access rule, calls the repository, and communicates whether the target was found and removed.

The HTTP operation exposes a deletion contract; it does not determine whether the underlying system performs a physical delete, a status change, or another domain-specific transition.

# References

[[aspnetcore3andreact.pdf]]
