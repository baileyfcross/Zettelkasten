2026-09-27 21:45

Status: #baby

Tags: [[Azure Network and Resilience Architecture]]

# Azure Routing Intent

Azure Virtual WAN routing intent declares that public traffic, private traffic, or both should pass through a designated security solution in a virtual hub. Virtual WAN then advertises the resulting default routes to connected spokes instead of requiring separate user-defined routes for each attachment. The policy simplifies consistent inspection, but it also changes reachability broadly and should be tested against service endpoints, private paths, and asymmetric-routing risks.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

