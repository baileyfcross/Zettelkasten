2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Protected Action

A protected action attaches a Microsoft Entra Conditional Access authentication context to a sensitive directory permission. Instead of applying only when a user begins a session, the additional policy is evaluated when the administrator attempts the protected operation.

This action-time check can require phishing-resistant authentication, a compliant device, or another context appropriate to the permission. It complements role assignment and [[Microsoft Entra Privileged Identity Management]]: PIM controls how a person obtains and activates a role, while the protected action can demand fresh evidence at the moment a high-impact permission is exercised. The control is most useful when the selected permission and policy are narrow enough not to block unrelated administration.

# References

[[masteringmicrosoftentraid.pdf]]
