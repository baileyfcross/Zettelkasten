2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# External Identity External Tenant

An External Identity external tenant is a Microsoft Entra directory dedicated to consumers of an organization's applications. It separates customer accounts, registered applications, sign-in methods, profile attributes, branding, and user journeys from the workforce tenant that contains employees.

The tenant can federate social, SAML, or OpenID Connect identity providers and can also issue local email-based credentials. Applications register through OIDC or SAML, while [[External Identity User Flow|user flows]] collect attributes and define self-service sign-up. Security includes smart lockout, Conditional Access, MFA, application roles, fraud-protection integrations, and monitoring. Because the directory stores consumer profile data, it should collect only information required for the application and avoid using identity attributes as a store for sensitive business records.

# References

[[masteringmicrosoftentraid.pdf]]
