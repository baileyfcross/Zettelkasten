2026-10-03 22:25

Status: #baby

Tags: [[Platform Security and Software Supply Chain]]

# Software Bill of Materials

A software bill of materials is a machine-readable inventory of the packages, libraries, images, and relationships included in a released software artifact. It is generated when the artifact and its dependencies are assembled so that the composition of that exact release can be examined later.

An SBOM does not prove that the components are safe. Its value comes from traceability: when a vulnerability is disclosed, teams can identify affected releases and prioritize remediation without rediscovering every dependency. The SBOM should be stored and associated with the immutable artifact it describes, then combined with scanning, policy, and audit workflows.

# References

[[platformengineeringforarchitects.pdf]]
