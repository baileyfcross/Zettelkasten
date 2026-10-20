2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Path-Specific Security Rule

A Helidon path-specific security rule applies security behavior to a route pattern and, optionally, selected HTTP methods. Patterns can identify one endpoint or a subtree such as `/user[/{*}]`, letting related paths share the same requirement.

Rules can require roles, allow optional authentication, or turn on auditing in addition to the server's defaults. This places access policy beside the route shape in configuration while leaving the handler focused on producing its response.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
