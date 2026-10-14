2026-10-11 21:26

Status: #baby

Tags: [[Docker Networking and Compose]]

# User-Defined Docker Network

A user-defined Docker network creates an explicit single-host communication boundary for selected containers. On a user-defined bridge, Docker's embedded DNS lets peers resolve container names instead of depending on addresses that may change after recreation.

Applications should use several narrowly scoped networks when tiers do not all need direct communication. Attaching a frontend, API, and database to only their required paths limits lateral reach after compromise and avoids exposing every service on the default bridge. Custom subnets must also avoid conflicts with host, VPN, and corporate networks.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
