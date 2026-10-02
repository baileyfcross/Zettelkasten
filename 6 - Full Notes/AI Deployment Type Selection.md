2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# AI Deployment Type Selection

AI deployment type selection matches a workload's interaction pattern to serverless, real-time, batch, workflow, or fully controlled infrastructure. The main constraints are latency, request volume, batch versus interactive use, custom logic, data sensitivity, compliance, cost, and operational capacity.

Low volume alone does not imply serverless if cold starts violate the service objective. Large scheduled workloads favor batch execution, while input validation and multi-step enrichment may justify a workflow endpoint. Sensitive workloads may require more controlled infrastructure despite its operational burden. The right choice satisfies mandatory constraints before optimizing price.

# References

[[microsoftfoundryinaction.pdf]]
