2026-09-27 22:21

Status: #baby

Tags: [[AWS Cloud Operations and Platform Engineering]] [[Developer Self-Service and Platform Experience]]

# Golden Path

A golden path is an opinionated, supported route for completing a common engineering task such as creating a service, deploying it, or adding observability. It packages working defaults, templates, automation, and documentation so teams do not have to rediscover every integration and control.

The path should be attractive because it is reliable and fast, not mandatory merely by decree. It belongs within an [[Internal Developer Platform]] and can evolve from user feedback. Well-defined exceptions preserve flexibility, while convergence on the common path lets the platform team improve security and operations once for many services.

Repository or software templates can encode ownership metadata, testing, deployment, observability, and security checks at the start of a component’s lifecycle. A portal can collect a few user choices and instantiate those expert-authored defaults, reducing manual adoption errors while keeping the generated configuration visible and maintainable.

# References

[[clouddevopsengineersguide.pdf]]

[[platformengineeringforarchitects.pdf]]
