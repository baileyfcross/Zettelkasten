2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# Jakarta Namespace Migration

Jakarta EE 9 replaced the Java EE `javax` package namespace with `jakarta` because the former name remained subject to Oracle branding. The project applied the change across the specifications together rather than migrating them one at a time.

Application imports therefore had to move, for example, from `javax.enterprise.context.ApplicationScoped` to its `jakarta.enterprise.context.ApplicationScoped` counterpart. Transformation tools could assist the mechanical migration, but libraries and runtime versions still had to align on the same namespace generation.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
