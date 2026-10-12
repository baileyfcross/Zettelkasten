2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]] [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Privileged Identity Management

Microsoft Entra Privileged Identity Management makes privileged roles eligible and time-bound instead of permanently active. Activation can require approval, multifactor authentication, justification, or a ticket, and the resulting events can be reviewed and audited. This limits standing privilege while preserving an operational path for administration. It does not remove the need for least-privilege role design, protected administrator accounts, access reviews, and monitored emergency procedures.

PIM distinguishes eligible assignments from active assignments and can govern Entra roles, Azure resource roles, and group membership or ownership. An eligible user activates a role for a bounded period; an approver can remain separate from the requester; audit history and alerts make the elevation observable. Discovery and insights helps convert permanent privileged assignments into eligible access, while recurring reviews remove privileges that are no longer justified.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[masteringmicrosoftentraid.pdf]]
