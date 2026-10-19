2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Apache Shiro Security Architecture

Apache Shiro organizes application security around a subject interacting with a security manager. Realms connect that manager to application-specific identity data, while authentication establishes the subject and authorization evaluates roles or fine-grained permissions. Shiro also provides session management and cryptographic utilities without requiring a full Jakarta EE container.

The framework's permission model can describe actions on resource types and instances more precisely than a single logged-in flag. In a social application, separate permissions can cover reading profiles, publishing content, moderating a community, and administering provider configuration. Shiro supplies the enforcement architecture, but external OAuth or social protocols may require an additional client library such as [[Scribe OAuth Client Library]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
