2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# Jakarta Security Identity Store

A Jakarta Security identity store validates credentials and retrieves the groups associated with a caller. It isolates the representation of users and groups from the HTTP authentication mechanism, allowing a mechanism to work with identity data held in a database, directory, or custom source.

Validation produces a result rather than granting unrestricted application access. The container and application still map the resulting principal and groups to roles and protected operations. This boundary makes it possible to replace credential storage without rewriting every request handler and to keep authentication distinct from [[Authorization]]. [[Jakarta Security Authentication Mechanisms]] handles the incoming exchange, while [[Jakarta Authorization Least Privilege]] constrains what an accepted identity can do.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
