2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Agent ID

Microsoft Entra Agent ID models an autonomous AI agent as a first-class identity rather than hiding it behind a shared application credential. A blueprint describes the agent pattern, a blueprint principal represents it in a tenant, and an agent identity represents a deployed instance; an optional agent user can support scenarios that require user-like interaction.

Registering these identities makes agents discoverable and gives security systems a stable subject for permissions, Conditional Access, risk evaluation, governance, and session revocation. The identity does not make an agent trustworthy by itself. Each instance still needs a narrow purpose, traceable owner, bounded tools and data, lifecycle controls, and removal when the agent or its blueprint is retired.

# References

[[masteringmicrosoftentraid.pdf]]
