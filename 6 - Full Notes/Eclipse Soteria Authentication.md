2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Eclipse Soteria Authentication

Eclipse Soteria is the reference implementation associated with Jakarta Security. It provides portable authentication mechanisms and identity-store integration so an enterprise application can express security behavior through Jakarta APIs instead of relying entirely on server-specific configuration.

Its mechanism-and-store separation is especially useful for social applications: protocol handling can change while the application's principal, group, and role model remains stable. Built-in form and basic mechanisms cover local sign-in, and custom mechanisms can bridge external protocols. [[Soteria OpenID Connect Authentication]] applies that extension point to federated login, while [[Jakarta Security Authentication Mechanisms]] describes the portable abstraction that Soteria implements.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
