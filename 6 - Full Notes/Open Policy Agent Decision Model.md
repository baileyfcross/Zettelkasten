2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Open Policy Agent Decision Model

Open Policy Agent receives structured input, evaluates it against Rego policy and locally available data, and returns a decision to a policy enforcement point. The application or admission component remains responsible for supplying the input and acting on the result.

Separating decision from enforcement makes policy reusable across systems, but OPA's in-memory data must be kept synchronized with authoritative sources. A decision is only as trustworthy as the input schema, policy version, supporting data, and failure behavior of the integration.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

