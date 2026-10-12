2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# Serverless AI Endpoint Cold Start

A serverless AI endpoint cold start is the delay incurred when no warm capacity is ready to handle an inference request. Serverless deployment minimizes idle infrastructure cost and simplifies prototypes or low-volume workloads, but the first request after inactivity may wait several seconds for capacity.

The delay can make serverless unsuitable for interactive systems even when monthly request volume is small. Latency objectives must therefore be evaluated at the tail and after idle periods, not only under warm tests. When a workload grows or requires consistently fast responses, a real-time managed endpoint with minimum replicas may be the more reliable choice.

# References

[[microsoftfoundryinaction.pdf]]
