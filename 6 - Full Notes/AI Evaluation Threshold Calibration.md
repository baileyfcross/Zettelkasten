2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# AI Evaluation Threshold Calibration

An evaluation threshold converts a continuous or categorical score into an operational decision, such as pass, review, block, or roll back. Its value should be calibrated against representative examples and the cost of both missed failures and false alarms, not selected merely because it produces an attractive pass rate.

Different metrics may require different thresholds because groundedness, relevance, safety, and coherence represent different risks. Teams should inspect examples close to each boundary, record why a cutoff is acceptable, and revisit it as the application, users, or data changes. A threshold is a governed decision rule rather than a universal fact.

# References

[[microsoftfoundryinaction.pdf]]
