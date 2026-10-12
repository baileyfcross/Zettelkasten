2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Linux Kernel Lockdown

Linux kernel lockdown is a security-module policy that restricts ways user space can modify or extract sensitive information from the running kernel. Integrity mode focuses on preventing unauthorized kernel modification, while a stricter confidentiality mode also blocks selected information disclosures.

Secure Boot can cause lockdown to become active, which may prevent an otherwise familiar unsigned module or low-level access path from working. The restriction protects the trust chain after boot, so development and deployment procedures must account for it instead of treating a failed module load as only a build problem.

# References

[[linuxkernelprogramming_secondedition.pdf]]
