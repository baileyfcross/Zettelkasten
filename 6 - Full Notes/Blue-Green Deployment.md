2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]] [[Microsoft Foundry Workflows and Deployment]]

# Blue-Green Deployment

Blue-green deployment maintains two equivalent production environments: one serves the current version while the other receives and verifies the new version. Traffic switches only when the new environment is ready.

The previous environment provides a rapid rollback path if the release fails. The technique reduces transition risk but requires duplicated capacity and careful management of shared data changes.

For a Foundry asset, the same principle means deploying a new model, prompt, workflow, or agent version beside the stable one, validating its endpoint and evaluation results, and only then moving callers. Directly modifying a live probabilistic asset removes the comparison and rollback evidence needed when behavior changes unexpectedly.

# References

[[agilegamedevelopment2e.pdf]]

[[microsoftfoundryinaction.pdf]]
