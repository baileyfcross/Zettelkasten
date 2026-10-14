2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Windows Server Security Baseline Drift

A Windows Server security baseline records the minimum approved configuration for a class of servers. Baseline drift is any intentional or accidental difference between that desired state and a host's current settings, such as disabled antivirus monitoring or a weakened access policy. Detecting drift converts security review from remembering what a server should look like into a repeatable comparison.

The baseline should be versioned, tied to the server's role, and checked regularly with management or scripting tools. For example, PowerShell can read a Microsoft Defender preference and compare it with the approved value, generating an alert when they differ. A finding still needs context: an authorized exception should be documented with an owner and expiration, while an unexplained change should trigger investigation and controlled remediation through mechanisms such as a [[Group Policy Object]].

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
