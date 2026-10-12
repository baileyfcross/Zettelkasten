2026-09-08 22:09

Status: #baby

Tags: [[Azure Logic Apps and Functions]]

# Azure Logic Apps

Azure Logic Apps is Microsoft's managed workflow service for assembling triggers, actions, conditions, loops, and service connectors. A logic app can be designed in the Azure portal or represented as deployable JSON inside a Visual Studio resource-group project.

The campaign project periodically reads rows from an Excel table, evaluates whether a message is due, posts it, and removes the processed row. The workflow remains visible as connected steps while a small Azure Function supplies date logic that the designer did not handle conveniently.

The Azure architecture map also uses Logic Apps as an integration and security-operations mechanism. Connectors and visual orchestration make them useful for cross-system workflows and Microsoft Sentinel playbooks, while functions remain appropriate for focused computation. Workflow state, connector identity, retry behavior, compensation, run-history sensitivity, and human approval steps must be designed because a visually simple flow can still carry privileged or irreversible effects.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
