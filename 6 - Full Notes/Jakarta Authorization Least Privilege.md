2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# Jakarta Authorization Least Privilege

Least privilege gives a principal only the permissions required for its current work. In a Jakarta enterprise application, roles and access constraints should separate ordinary use, administration, publication, and integration tasks rather than treating successful authentication as universal authority.

The source also emphasizes granularity: access may need to be restricted by operation, resource instance, attribute, or time. A social integration that can read a public profile need not receive permission to publish, administer a community, or retain private messages. Declarative role constraints establish broad boundaries, while programmatic checks can enforce finer conditions. This makes [[Jakarta EE Declarative and Programmatic Security]] a pair of enforcement styles for the same least-privilege objective.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
