2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]]

# Azure Firewall TLS Inspection

Azure Firewall TLS inspection decrypts selected encrypted traffic, applies inspection controls, and establishes a new TLS connection to the destination. This intermediary pattern requires a trusted private certificate authority for outbound inspection and careful certificate handling for inbound scenarios. It increases visibility but also introduces privacy, compatibility, performance, and trust-distribution concerns, so exclusions, capacity, certificate lifecycle, and failure behavior must be designed explicitly.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
