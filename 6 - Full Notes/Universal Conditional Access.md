2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# Universal Conditional Access

Universal Conditional Access extends Microsoft Entra policy enforcement from modern cloud applications to traffic acquired by Global Secure Access. A policy can target internet resources, Microsoft traffic, or private applications and require controls such as multifactor authentication, compliant devices, acceptable risk, or an approved network.

This is especially valuable for private or legacy resources that cannot interpret Entra tokens themselves: the identity-aware access path enforces policy before traffic reaches them. A compliant-network check can require the Global Secure Access client or a configured remote network, reducing token replay from an unmanaged path. Because the network service becomes part of policy evaluation, signaling, forwarding profiles, exclusions, and emergency recovery must be tested together before enforcement.

# References

[[masteringmicrosoftentraid.pdf]]
