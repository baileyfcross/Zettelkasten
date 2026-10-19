2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# MicroProfile JWT Container Integration

MicroProfile JWT Authentication standardizes how a bearer JWT becomes an authenticated identity inside a microservice. After validating the token, the runtime exposes its subject and claims through the container security context so application code can use familiar principal and role-based checks.

The source highlights two useful mappings: the `upn` claim can identify the caller principal, and the `groups` claim can supply role membership. These mappings let independently deployed Jakarta services interpret identity consistently without inventing a different token-to-role convention for every endpoint. They do not excuse incomplete validation: [[JWT Claim and Signature Structure|signature, issuer, audience, and lifetime checks]] must precede authorization, and roles should still follow [[Jakarta Authorization Least Privilege]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
