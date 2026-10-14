2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Emergency Access Account

An emergency access account is a cloud-only administrative identity reserved for recovering a Microsoft Entra tenant when normal administrator sign-in, federation, multifactor services, or privileged-role approval paths are unavailable. It is commonly called a break-glass account because routine work should never depend on it.

The account should use the tenant's onmicrosoft.com domain, hold permanent Global Administrator access, and remain independent of on-premises synchronization. Strong phishing-resistant authentication, securely stored recovery material, dedicated secure workstations, and alerts on every sign-in reduce the danger of that standing privilege. Organizations normally maintain two independent accounts and test them regularly; an emergency path that has silently expired is not a recovery control.

# References

[[masteringmicrosoftentraid.pdf]]
