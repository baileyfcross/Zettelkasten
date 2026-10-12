2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]] [[Platform Delivery and Artifact Automation]]

# GitOps Pull-Based Deployment

GitOps pull-based deployment places the component that applies production state inside the managed environment. The component watches a repository and pulls a newly approved desired state, inverting a push pipeline that connects from CI and runs commands directly against production.

The inversion reduces the need to store cluster-administration credentials in the build system. CI prepares artifacts and validates definitions, while the [[GitOps Operator]] controls application inside its narrower trust boundary. The model may add a short polling delay, but webhook notification can reduce that latency without turning CI back into the deployment authority.

Pull-based deployment also separates artifact creation from release promotion. A reviewed desired-state change selects an existing artifact for an environment, and the local reconciler applies it; this preserves the identity of what was tested while keeping the target’s live state under continuous comparison.

# References

[[clouddevopsengineersguide.pdf]]

[[platformengineeringforarchitects.pdf]]
