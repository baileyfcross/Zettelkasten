2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# Secure Boot Shim Verification

In a Secure Boot configuration, firmware verifies an accepted first-stage loader and the SLES shim participates in the trust chain used to load GRUB and approved kernel components. Each stage limits execution to content whose signature is accepted by the current policy.

The chain affects custom kernels and drivers: code that is technically valid may still be rejected because it lacks an accepted signature. Disabling verification changes the platform trust boundary, so a secure deployment should instead plan how locally built components are signed and enrolled.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
