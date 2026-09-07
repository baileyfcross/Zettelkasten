2026-09-06 20:52

Status: #baby

Tags: [[Web Identity and Access Control]]

# Custom Authorization Policy

A custom authorization policy expresses an application-specific access rule beyond the presence of a valid identity. It can require selected claims or other conditions and is registered under a name used by protected endpoints.

Centralizing the rule makes its intent inspectable and consistent. The policy is enforced on the server even when the React client also hides or disables the corresponding operation.

# References

[[aspnetcore3andreact.pdf]]
