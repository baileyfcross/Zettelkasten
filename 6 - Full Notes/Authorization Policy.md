2026-09-06 20:52

Status: #baby

Tags: [[Web Identity and Access Control]]

# Authorization Policy

An authorization policy is a named set of requirements that an authenticated request must satisfy before protected ASP.NET Core code runs. A controller or action can reference the policy declaratively instead of repeating access checks in its body.

Policies keep permission logic separate from HTTP coordination and can be reused across endpoints. Authentication establishes the principal evaluated by the policy; it does not by itself guarantee authorization.

# References

[[aspnetcore3andreact.pdf]]
