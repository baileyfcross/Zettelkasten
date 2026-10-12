2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Signing

Kernel module signing attaches a cryptographic signature to a module so the kernel can verify that the object was approved by a trusted key. Verification protects the privileged extension boundary from unauthorized or modified binaries.

A permissive policy may report verification failure while still allowing a load and marking the kernel tainted; an enforcing policy rejects an untrusted module. The mechanism establishes provenance and integrity, but it does not prove that signed code is free of defects.

# References

[[linuxkernelprogramming_secondedition.pdf]]
