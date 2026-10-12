2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Entra User and Sign-In Risk

Microsoft Entra distinguishes user risk from sign-in risk. User risk is the cumulative likelihood that an identity has been compromised, while sign-in risk is the likelihood that a particular authentication attempt was made by someone other than the account owner.

Sign-in risk is event-specific and can be remediated when the legitimate user completes a strong authentication challenge. User risk persists across events and commonly requires a secure password reset or an administrative investigation. Both are classified as low, medium, or high based on detection confidence, and some evidence is calculated in real time while other evidence arrives after deeper offline analysis. Keeping the two signals separate allows [[Risk-Based Conditional Access]] to match the response to the kind of risk.

# References

[[masteringmicrosoftentraid.pdf]]
