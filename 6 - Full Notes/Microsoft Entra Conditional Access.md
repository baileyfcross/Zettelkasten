2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]] [[Microsoft Entra Identity and Authentication]]

# Microsoft Entra Conditional Access

Microsoft Entra Conditional Access evaluates signals such as user, application, device state, location, and risk before granting access. Policies can require stronger authentication, demand a compliant device, restrict a session, or block a request. Because multiple policies combine, effective design starts with explicit personas and protected resources, uses report-only evaluation, preserves emergency access, and avoids creating gaps or accidental lockouts through overlapping exceptions.

The policy engine separates assignments, conditions, and access controls. Assignments identify users and target resources; conditions refine the match with device, location, client, authentication context, or risk; grant and session controls determine the result. Policies are evaluated together rather than in an ordered first-match list, so a design must account for their combined effect and exclude monitored emergency accounts before enforcement.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[masteringmicrosoftentraid.pdf]]
