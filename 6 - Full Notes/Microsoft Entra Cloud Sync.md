2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Microsoft Entra Cloud Sync

Microsoft Entra Cloud Sync provisions identities from on-premises Active Directory into Entra ID through lightweight agents and a cloud-managed configuration. The outbound agents connect directory data to the cloud provisioning service, which applies mappings and synchronization rules without requiring the full Entra Connect engine on one large on-premises server.

The model supports multiple disconnected forests and simplifies deployment and availability by allowing several agents. Entra Connect Sync remains relevant for advanced scenarios and features that Cloud Sync does not cover, so the choice should follow forest topology, object and group requirements, filtering, writeback, and operational needs. In either case, synchronization is the bridge for [[Hybrid Identity]] and does not itself select the user's cloud authentication method.

# References

[[masteringmicrosoftentraid.pdf]]
