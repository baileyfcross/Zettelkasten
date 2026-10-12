2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# Microsoft Foundry Workflow Endpoint

A Microsoft Foundry workflow endpoint exposes an orchestrated process as one callable application interface. The caller submits an input to the workflow rather than separately invoking validation, retrieval, model, transformation, and formatting services.

The endpoint is appropriate when every request should follow consistent preprocessing, branching, enrichment, and output rules. It simplifies clients and centralizes behavioral updates, but also makes the workflow's timeout, schema, and dependency failures part of one production contract. Publishing should therefore follow end-to-end testing of every important branch, not only direct testing of the underlying model.

# References

[[microsoftfoundryinaction.pdf]]
