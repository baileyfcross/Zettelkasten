2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra External and Network Access]]

# External Identity User Flow

An External Identity user flow defines the self-service sign-up and sign-in journey for applications in a Microsoft Entra external tenant. It selects accepted identity providers, associates applications, and specifies the built-in or custom profile attributes collected from a consumer.

One flow can serve several applications, but an application is associated with one flow. Branding and page layout shape the visible experience, while custom authentication extensions can validate submitted attributes, block ineligible registrations, send branded one-time-passcode messages, or add claims before token issuance. Each extension creates a synchronous dependency on external logic, so error handling, privacy, and availability must be designed as part of the authentication path rather than as cosmetic customization.

# References

[[masteringmicrosoftentraid.pdf]]
