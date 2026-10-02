2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# AI Evaluation Metric Selection

AI evaluation metrics should correspond to the application’s actual failure modes. A retrieval-grounded assistant may need relevance and groundedness measures, a conversational agent may also need coherence and intent resolution, and a public-facing system may require explicit safety evaluators. Using every available metric can add cost without improving a decision.

Selection begins with the behavior that matters, the consequence of failure, and the evidence each evaluator can provide. The resulting metric set should be small enough to interpret but broad enough to catch distinct risks. Operational latency and cost belong beside behavioral quality rather than substituting for it.

# References

[[microsoftfoundryinaction.pdf]]
