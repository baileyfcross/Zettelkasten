2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Windows Defender Firewall

Windows Defender Firewall with Advanced Security filters inbound and outbound host traffic by profile, protocol, port, program, service, address, and authentication properties. Domain, Private, and Public profiles let one server apply different rules as its network classification changes. The advanced console and Group Policy expose more precise controls than the simplified Windows Security or Control Panel views.

Host filtering remains valuable behind a perimeter firewall because it limits lateral movement and protects a server when network placement or another control fails. Broadly disabling the firewall removes that layer and can conceal a missing application rule. Administrators should define explicit workload requirements, deploy policy centrally, log relevant drops, and verify which profile each interface selected. A domain server that starts without contacting a controller may select another profile and behave differently until classification is corrected.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
