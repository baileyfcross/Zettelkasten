2026-09-05 16:28

Status: #baby

Tags: [[Machine Learning Foundations]]

# Federated Learning

Federated learning trains a shared model by sending the model to participating devices, updating it on local data, and aggregating model changes rather than collecting the raw examples centrally.

For assistants, this can reduce the amount of private speech or interaction data transferred off a device. It does not eliminate every privacy risk, but it changes the training architecture so personal data can remain local.

The book also describes the architecture for phones and hospitals contributing to a shared project: a local model learns from each site's records, and an aggregator combines updates to improve a central model. Sharing model changes rather than raw records reduces central collection but does not, by itself, settle every disclosure risk.

Alpaydin places federated learning among privacy-preserving approaches: each participant trains its own model on local records and shares parameter updates with the others. The architecture changes what leaves the data holder, but the update channel still needs security and a privacy analysis; local retention is not equivalent to a guarantee that no information can leak.

# References

[[aiassistants.epub]]

[[datascience_mit.epub]]

[[machinelearning_mit.epub]]
