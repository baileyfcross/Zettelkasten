2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# Microsoft Foundry Deployment Readiness Check

A Microsoft Foundry deployment readiness check verifies the model, workflow, agent, environment, access, and test evidence before an asset is published. Inputs and outputs must match their schemas, workflow nodes must be connected, agent tools and knowledge sources must respond, and required users or identities must have the correct permissions.

Readiness also includes representative functional, edge-case, safety, and load tests rather than one successful playground exchange. A deployable asset needs a version, endpoint settings, access policy, monitoring destination, and rollback path. Treating these checks as a release gate prevents a valid portal configuration from being mistaken for a production-ready system.

# References

[[microsoftfoundryinaction.pdf]]
