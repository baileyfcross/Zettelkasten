2026-10-03 22:25

Status: #baby

Tags: [[Platform Security and Software Supply Chain]]

# CI-CD Pipeline Security

CI-CD pipeline security protects the path from source change to deployed artifact. Controls can include protected main branches, signed commits, code-owner review, secret detection, automated tests, dependency scanning, narrowly scoped credentials, and continuous inspection of repositories and artifacts.

The pipeline is part of the software supply chain and should not receive broad production authority merely because it builds trusted code. Pull-based deployment can localize deployment credentials inside the target environment, while immutable artifacts and reviewed desired state separate creation from release authority. Every automation identity should be auditable and limited to the action it performs.

# References

[[platformengineeringforarchitects.pdf]]
