2026-09-30 23:37

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory Sites and Services

Active Directory Sites and Services maps IP subnets to physical or network locations and associates domain controllers with those sites. The mapping helps clients locate a nearby controller and lets the directory distinguish fast local replication from traffic that crosses slower or costly links.

Sites should describe network topology, not merely repeat the organizational-unit tree. Missing or incorrect subnet definitions can send authentication and replication traffic across the wrong connection. Site links and their schedules or costs then guide intersite replication. Maintaining this topology becomes more important as a domain spans branches, datacenters, or cloud networks because directory behavior depends on the administrator's model of connectivity.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
