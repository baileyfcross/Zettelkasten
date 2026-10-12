2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]] [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Continuous Access Evaluation

Microsoft Entra Continuous Access Evaluation allows supported applications to react to critical identity events before a normal access token expires. Account disablement, password changes, elevated user risk, and policy-relevant network changes can therefore interrupt an active session more quickly. The capability depends on cooperation between the identity provider and resource service, so architects should verify workload support and should not treat it as a substitute for session controls, token protection, or application authorization.

For workload identities, CAE can enforce location and risk changes against supported Microsoft Graph requests and revoke access after a service principal is disabled, deleted, or judged high risk. The client must declare the relevant capability and reauthenticate after a claims challenge. This shows that continuous evaluation is a protocol cooperation among issuer, client, and resource, not a blanket property of every token-bearing application.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[masteringmicrosoftentraid.pdf]]
