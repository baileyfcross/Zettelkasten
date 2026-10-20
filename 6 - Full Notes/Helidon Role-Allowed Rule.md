2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Role-Allowed Rule

A Helidon `roles-allowed` rule restricts a configured path to authenticated subjects holding at least one permitted role. The example assigns a `user` role to a route family and an `admin` role to a more privileged endpoint.

Authentication alone does not satisfy this rule: a configured user with an empty role list can log in but cannot access either protected area. The route policy therefore separates proof of identity from authorization to perform a particular operation.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
