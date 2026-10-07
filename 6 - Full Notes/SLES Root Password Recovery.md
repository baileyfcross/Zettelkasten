2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# SLES Root Password Recovery

SLES root-password recovery uses temporary boot parameters to enter a privileged early or reduced environment, prepare the real root filesystem for changes, and set a new credential. The exact steps depend on how far the boot process can proceed and whether storage, encryption, or mandatory policy requires additional handling.

Physical or console control over the bootloader can therefore become administrative control over the system. Firmware and bootloader protection, disk encryption, and documented custody of recovery access are part of the security model. After recovery, temporary parameters must be removed and normal boot and authentication verified.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
