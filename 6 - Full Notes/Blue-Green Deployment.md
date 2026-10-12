2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]] [[Microsoft Foundry Workflows and Deployment]]

# Blue-Green Deployment

Blue-green deployment maintains two equivalent production environments: one serves the current version while the other receives and verifies the new version. Traffic switches only when the new environment is ready.

The previous environment provides a rapid rollback path if the release fails. The technique reduces transition risk but requires duplicated capacity and careful management of shared data changes.

For a Foundry asset, the same principle means deploying a new model, prompt, workflow, or agent version beside the stable one, validating its endpoint and evaluation results, and only then moving callers. Directly modifying a live probabilistic asset removes the comparison and rollback evidence needed when behavior changes unexpectedly.

On Kubernetes, blue and green Deployments can coexist behind a stable Service whose selector determines which version receives production traffic. Switching the selector is fast, but database compatibility, in-flight work, capacity, and post-switch observation still determine whether rollback is truly safe.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[agilegamedevelopment2e.pdf]]

[[microsoftfoundryinaction.pdf]]
