2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security Request Authorization Rules

Spring Security request authorization rules are declared in a `SecurityFilterChain` before a request reaches application code. Matchers can combine a path and HTTP method, permit selected public endpoints, require an exact authority or role for sensitive operations, and finish with an authenticated catch-all rule.

The final catch-all protects a newly added route that a developer forgot to mention explicitly. Role checks conventionally add the `ROLE_` prefix, while authority checks compare the exact granted value, including OAuth scope authorities. URL rules establish the outer gate; [[Spring Security Method Authorization]] can enforce an operation or object-specific rule again at the service boundary.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
