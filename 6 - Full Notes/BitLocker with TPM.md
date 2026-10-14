2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# BitLocker with TPM

BitLocker encrypts a Windows volume so data at rest is not readable merely by removing the drive or booting another operating system. A Trusted Platform Module can seal key release to expected boot measurements, allowing normal startup while withholding the volume key when the platform state appears to have been altered.

TPM use does not eliminate recovery planning. Recovery information must be escrowed somewhere administrators can reach when hardware, firmware, or boot configuration changes prevent automatic unlock. Additional startup authentication can raise assurance but also increase unattended-restart and remote-recovery complexity. BitLocker protects offline storage; once an authorized system is running and the volume is unlocked, file permissions, credential security, backups, and application controls still govern access.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
