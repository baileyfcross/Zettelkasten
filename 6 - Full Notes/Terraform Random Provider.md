2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Random Provider

The Terraform random provider creates values such as strings, identifiers, integers, passwords, or shuffled selections and then records the result in [[Terraform State]]. The value is generated when the resource is created and remains stable across later applies until its arguments or replacement triggers require regeneration.

That persistence distinguishes a random resource from an ordinary language function evaluated afresh. It is useful for globally unique names or selecting zones, but a generated password remains sensitive even when display is suppressed because the value is stored in state. Backend protections therefore apply to random secrets as strongly as to provider-returned credentials.

# References

[[masteringterraform.pdf]]

