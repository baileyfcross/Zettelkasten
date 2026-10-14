2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]] [[.NET Cryptography and Access Control]] [[Cloud Security and Data Protection]] [[Cybersecurity Goals and Trust]] [[TLS Authentication and Secure Remote Access]] [[Microsoft Entra Identity and Authentication]]

# Authorization

Authorization determines whether an identified client is permitted to access a resource or perform an operation. It follows [[Authentication]] because a policy needs a known user, role, or claim on which to base its decision.

Angular route guards can control client navigation, but server-side authorization must protect the corresponding API action. A hidden view is not a secure boundary when a caller can issue its own request.

The stock-checker assigns different read and update capabilities to authenticated users through roles and protected operations. This demonstrates that successful login is not sufficient authority for every feature exposed by an application.

For cloud resources, authorization applies after identity and authentication have been established. It can grant rights according to a user's role and should restrict both human users and automated applications to the operations their work requires.

The cybersecurity model distinguishes authorization from authentication: proving who a user is does not prove that the user may reach every resource. Access-control policy can base authorization on administrator mandates, owner discretion, roles, or contextual rules.

The design-patterns source extends the inventory web application so logged-in users are not automatically permitted to perform every product action. Restricted pages and operations require a role or policy check on the server; the cloud discussion makes the same distinction when an external identity provider supplies a token but the application retains its own access rules.

In Microsoft Entra, authorization is expressed through directory roles, Azure resource roles, application roles, group membership, scopes, and claims. The security principal identifies the user or workload, the role definition states permitted operations, and the assignment binds that authority to a scope. Conditional Access can decide whether a session may begin, but the receiving service must still enforce what the authenticated principal is allowed to do.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cloudcomputing_mit.epub]]

[[cybersecurity.epub]]
[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[masteringmicrosoftentraid.pdf]]
