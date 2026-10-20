2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon HTTP Basic User Store

Helidon's HTTP Basic authentication provider can define users, passwords, and role arrays in the security configuration tree. Nested numeric path segments select entries from provider and user lists, allowing code to retrieve a configured login or its associated roles through `Config`.

The example permits clear-text passwords only because `require-encryption` is false and explicitly warns that production configuration should require encryption. User-role data then becomes the source for [[Helidon Role-Allowed Rule]] decisions.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
