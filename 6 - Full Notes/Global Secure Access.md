2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# Global Secure Access

Global Secure Access is Microsoft's identity-aware Secure Service Edge formed by [[Microsoft Entra Internet Access]] and [[Microsoft Entra Private Access]]. It routes selected traffic through Microsoft points of presence so identity, device, network, and destination signals can participate in a common Zero Trust access decision.

The Global Secure Access client acquires traffic from user devices, while remote-network IPSec connections can acquire traffic for branch offices. Forwarding profiles distinguish Microsoft, internet, and private traffic. Dashboards, traffic logs, health logs, and alerts make the resulting access fabric observable. The service joins policy and path, but deployment still requires explicit routing, role separation, connector health, exclusions, and fallback plans so a policy or tunnel failure does not become an unexplained outage.

# References

[[masteringmicrosoftentraid.pdf]]
