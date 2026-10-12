2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Deployment Architecture]]

# Kubernetes RAG Application Architecture

A Kubernetes RAG application separates the user-facing service, retrieval logic, vector database, and language-model endpoint into independently deployable components. Services provide stable names while Deployments let each component scale and roll out according to its own resource profile.

The separation makes network policy and identity explicit. The frontend should reach the RAG API, the RAG API should reach the approved vector and model endpoints, and unrelated pods should not inherit those data paths merely because they share a cluster.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

