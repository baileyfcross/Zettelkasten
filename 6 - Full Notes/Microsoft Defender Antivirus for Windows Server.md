2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Microsoft Defender Antivirus for Windows Server

Microsoft Defender Antivirus protects a Windows Server host by continuously scanning for malware and ransomware, combining signatures, cloud intelligence, machine-learning detection, and behavioral analysis. When it identifies malicious software, automated response can quarantine or remove the threat, while alerts and reports give administrators evidence for investigation and policy refinement.

The control is complementary to [[Microsoft Defender for Identity]]: antivirus observes files and activity on the server endpoint, whereas Defender for Identity focuses on identity signals and directory-related attacks. Windows Admin Center can provide a unified management surface for scans, settings, and threat status. Its configuration should be compared with a documented [[Windows Server Security Baseline Drift|security baseline]] so that disabled real-time protection or other weakening changes are detected rather than silently accepted.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
