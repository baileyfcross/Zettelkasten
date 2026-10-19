2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# Jakarta EE Declarative and Programmatic Security

Jakarta EE applications can express security declaratively in deployment metadata or annotations, or make programmatic checks through security APIs. Declarative constraints associate roles and access rules with application resources without embedding the entire decision process in business code. Programmatic security is useful when the decision depends on runtime state that static constraints cannot fully describe.

The two styles are complementary. Stable entry-point rules belong in declarative policy, while context-sensitive decisions may use the caller principal or role checks inside the application. In either case, the server—not a browser interface—must enforce the boundary. [[Jakarta Security Authentication Mechanisms]] establishes the caller identity and [[Jakarta Authorization Least Privilege]] guides the permissions that identity receives.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
