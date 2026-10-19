2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Spring Security Provider and Filter Chains

Spring Security processes web security through a chain of filters that recognize credentials or protocol messages, create authentication requests, and place an accepted identity into the security context. Authentication providers perform the matching validation for a credential type or identity source.

This layered design allows password login, bearer tokens, and external-provider login to coexist without one monolithic handler. Ordering and endpoint matching matter because a request must reach the intended filter and authorization rule. Once authentication succeeds, authorities inform access decisions; they should not be granted simply because a provider supplied a profile. [[Spring Security OAuth Social Login]] specializes this pipeline for OAuth 2.0 and OpenID Connect providers.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
