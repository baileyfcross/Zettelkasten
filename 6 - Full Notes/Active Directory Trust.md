2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory Trust

An Active Directory trust allows identities authenticated in one domain to be recognized for resource access in another. Trust direction defines which domain accepts the other's identities, and a two-way trust establishes recognition in both directions. Domains created in the same forest receive built-in trust relationships, while separate forests may need an explicit trust for collaboration or migration.

Trust does not automatically grant access to every resource; it creates a path through which permissions can be assigned. Name resolution between the domains must also work, often through conditional DNS forwarding. Acquisition and staged migration are common uses because both directories can remain online while administrators grant controlled cross-domain access and move identities or services gradually.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
