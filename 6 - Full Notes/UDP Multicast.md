2026-09-22 23:34

Status: #baby

Tags: [[TCP UDP and Internet Protocol Addressing]]

# UDP Multicast

UDP multicast sends a datagram to a multicast group address so several subscribed receivers can obtain the same packet. A sender does not establish a separate reliable connection with every recipient.

This supports one-to-many discovery or distribution with low transport overhead. Delivery, ordering, and group membership changes are not guaranteed like a TCP session, so the application must tolerate missing or duplicated messages when those outcomes matter.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
