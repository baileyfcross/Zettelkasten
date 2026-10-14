2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Upgrade Strategy

A Terraform upgrade strategy treats the CLI, providers, and modules as separate but interacting versioned dependencies. A new Terraform release can change supported provider ranges; a provider release can deprecate resource arguments; and a module release can change its public interface or resource addresses.

Versions should be constrained and upgraded purposefully rather than following every release or stagnating until an emergency. The [[Terraform Plan]] exposes many configuration effects, while representative test deployments catch behavior that appears only against a live API. Updating one layer at a time narrows diagnosis, and [[Terraform State Refactoring]] may be required when a module reorganizes existing resource addresses without intending replacement.

# References

[[masteringterraform.pdf]]

