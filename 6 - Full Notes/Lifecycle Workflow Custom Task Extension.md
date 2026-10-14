2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Lifecycle Workflow Custom Task Extension

A Lifecycle Workflow custom task extension lets a Microsoft Entra workflow invoke organization-specific logic implemented with Azure Logic Apps. It fills gaps where built-in lifecycle tasks cannot update a proprietary system, call an external service, or perform a specialized business process.

A launch-and-continue extension starts the Logic App without holding the workflow, while launch-and-wait pauses until the extension reports a result. The latter creates a coordination boundary: the external process must authenticate with its managed identity, correlate the request, return success or failure, and handle timeouts or retries. Custom extensions increase reach but also expand the failure surface, so workflow history and idempotent external actions are essential.

# References

[[masteringmicrosoftentraid.pdf]]
