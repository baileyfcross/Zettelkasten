2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Pull-Based Deployment

GitOps pull-based deployment places the component that applies production state inside the managed environment. The component watches a repository and pulls a newly approved desired state, inverting a push pipeline that connects from CI and runs commands directly against production.

The inversion reduces the need to store cluster-administration credentials in the build system. CI prepares artifacts and validates definitions, while the [[GitOps Operator]] controls application inside its narrower trust boundary. The model may add a short polling delay, but webhook notification can reduce that latency without turning CI back into the deployment authority.

# References

[[clouddevopsengineersguide.pdf]]

