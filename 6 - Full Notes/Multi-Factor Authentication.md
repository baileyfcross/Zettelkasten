2026-09-14 02:44

Status: #baby

Tags: [[Everyday Cybersecurity Applications]] [[Microsoft Entra Identity and Authentication]]

# Multi-Factor Authentication

Multi-factor authentication requires evidence from more than one [[Authentication Factor Categories|factor category]], such as something known, possessed, or inherent to the user. Combining independent categories makes a stolen password insufficient by itself.

[[Two-Factor Authentication]] is the common case using exactly two categories. Adding steps improves protection only when the factors are genuinely independent and the process remains usable enough that people follow it.

Microsoft Entra can require MFA during ordinary sign-in, privileged-role activation, or a risky session. System-preferred authentication presents the strongest method a user has registered, and authentication strengths let policy require phishing-resistant methods for sensitive access. MFA registration must be planned before risk-based policies depend on it, and stolen session tokens remain a separate threat that continuous evaluation and token-aware controls must address.

# References

[[cybersecurity.epub]]

[[masteringmicrosoftentraid.pdf]]
