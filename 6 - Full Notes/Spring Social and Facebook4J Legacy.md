2026-10-18 22:56

Status: #baby

Tags: [[Java Social Platform SDKs]]

# Spring Social and Facebook4J Legacy

Spring Social provided a Spring programming model for connecting user accounts to social providers, while Facebook4J offered a Java-specific wrapper for Facebook APIs. Both reduced the amount of direct protocol and HTTP work required by applications built against the provider landscape of their time.

The source treats these projects as legacy examples rather than default choices for a new integration. Their history shows that a polished abstraction can become unusable when its maintenance stops or the provider removes the API generation it represents. Existing systems may still need them during migration, but new work should verify current support and prefer maintained protocols or SDKs. [[Agorava Social Framework]] reflects a related multi-provider effort, and [[Meta Business SDK for Java]] represents a current vendor-specific direction.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
