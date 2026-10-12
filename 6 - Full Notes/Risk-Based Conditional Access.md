2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Risk-Based Conditional Access

Risk-based Conditional Access uses [[Entra User and Sign-In Risk|user or sign-in risk]] from Microsoft Entra ID Protection as policy conditions. A sign-in-risk policy can require strong authentication for a suspicious attempt, while a user-risk policy can require secure password change or block an account believed to be compromised.

Successful completion of the required control can self-remediate the corresponding risk, reducing the delay and workload of a manual investigation. Separate policies are clearer because user and sign-in risk describe different conditions. Deployment should first register users for MFA and self-service password reset, preserve [[Emergency Access Account|emergency accounts]], define trusted network locations, and test in report-only or impact-analysis views before enforcement.

# References

[[masteringmicrosoftentraid.pdf]]
