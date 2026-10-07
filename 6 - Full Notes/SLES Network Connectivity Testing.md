2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# SLES Network Connectivity Testing

Network troubleshooting on SLES is most useful when it moves through layers: confirm link and device state, inspect the assigned address and routes, verify the selected gateway, test name resolution, then test the destination port or application protocol. Each result narrows the failed boundary without assuming every timeout is a firewall problem.

The test must also run from the relevant network namespace and host. Local success may not represent a remote client, and an ICMP response does not prove a TCP service is listening. Capturing the source, destination, resolved address, and port makes the evidence reproducible.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
