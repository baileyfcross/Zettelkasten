2026-10-03 16:51

Status: #baby

Tags: [[GenAIOps Pipeline Automation]]

# Apache Airflow DAG

An Apache Airflow DAG is a directed acyclic graph of ordered workflow tasks. Nodes can represent ingestion, validation, training, evaluation, registration, batch inference, or notification, while edges state which tasks must finish before others can begin.

The graph remains acyclic; repetition comes from scheduling a new run rather than linking the last task back to the first. Airflow records task status, retries transient failures, and preserves execution history, while the actual compute can run in containers, Kubernetes, or other external systems.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

