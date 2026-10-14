2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Connection Broker

Remote Desktop Connection Broker maintains the relationship among users, collections, and Remote Desktop Session Hosts. It distributes new connections across eligible hosts and reconnects a returning user to an existing disconnected session instead of creating a duplicate session elsewhere.

The broker is the coordination layer, not the host that runs the user's application. Its availability becomes important as soon as a deployment contains multiple Session Hosts or depends on stable reconnection. Server Manager can install the broker together with Web Access and Session Host roles in a standard deployment. Production designs should separate responsibilities as scale grows, protect the broker's database and name, and validate reconnection and load distribution before treating the farm as redundant.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
