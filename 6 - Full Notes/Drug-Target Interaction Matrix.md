2026-09-28 03:43

Status: #baby

Tags: [[Pharmaceutical Discovery Analytics]]

# Drug-Target Interaction Matrix

A drug-target interaction matrix places drugs in rows and targets in columns. A value of one records an experimentally verified interaction, while a zero means the pair is unknown rather than proven not to interact.

The matrix supports recommendation-style modeling: drugs and targets are embedded into a [[Shared Drug-Target Latent Space]], and unknown entries receive predicted probabilities. Evaluation must preserve the difference between predicting a missing pair and generalizing to an entirely unseen row or column.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

