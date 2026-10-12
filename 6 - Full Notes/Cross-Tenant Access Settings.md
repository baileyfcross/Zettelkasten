2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# Cross-Tenant Access Settings

Cross-tenant access settings control B2B collaboration between Microsoft Entra organizations. Inbound settings determine which external users and applications may enter a resource tenant; outbound settings determine which local users and external resources may be reached in another tenant.

Default rules establish the baseline, and organization-specific rules override them for named partners. Trust settings can accept multifactor or compliant-device claims from a partner, automatic redemption can suppress repeated consent when both tenants agree, and tenant restrictions can stop managed users or devices from reaching unapproved external tenants. These controls express reciprocal trust, so both the home and resource organization must understand which identity evidence is being relied upon.

# References

[[masteringmicrosoftentraid.pdf]]
