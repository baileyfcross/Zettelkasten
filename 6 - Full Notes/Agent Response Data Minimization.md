2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Agent Response Data Minimization

Agent response data minimization restricts an answer to the fields and detail needed for the user’s stated task. A downstream tool may return a large record or analytical result, but successful authorization does not mean every returned value should be placed in model context, displayed to the user, or retained in traces.

Minimization can occur in the tool query, response schema, transformation step, prompt, and final rendering. Teams should prefer aggregates or selected fields when they satisfy the request, remove unnecessary identifiers, and evaluate leakage cases. This reduces exposure while also giving the model a smaller and more relevant evidence set.

# References

[[microsoftfoundryinaction.pdf]]
