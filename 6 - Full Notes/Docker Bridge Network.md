2026-10-11 21:26

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Bridge Network

A Docker bridge network connects container network namespaces to a Linux bridge on one host. Virtual Ethernet interfaces join each container to the bridge, Docker assigns addresses from the network subnet, and host routing or network address translation provides permitted external connectivity.

The automatically created default bridge offers basic connectivity but is a broad shared boundary. A bridge has local scope and cannot itself span several Docker hosts, so multi-node service reachability requires an orchestration or overlay mechanism rather than treating the single-host subnet as cluster networking.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
