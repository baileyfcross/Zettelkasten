2026-09-27 21:45

Status: #baby

Tags: [[Azure Network and Resilience Architecture]]

# Azure Hub-and-Spoke Network

An Azure hub-and-spoke network places shared connectivity, routing, DNS, and inspection services in a hub virtual network while application workloads occupy peered spoke networks. The topology avoids duplicating common controls and gives landing zones a standard attachment point. Peering is not transitive by default, so routes and network appliances must deliberately provide traffic paths; centralization also makes hub capacity and policy a shared blast-radius concern.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

