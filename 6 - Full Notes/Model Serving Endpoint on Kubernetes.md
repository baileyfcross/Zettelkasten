2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Deployment Architecture]]

# Model Serving Endpoint on Kubernetes

A model serving endpoint exposes real-time or batch inference through a framework such as KServe, Ray Serve, or Seldon Core. Kubernetes supplies scheduling, Service discovery, rollout, and autoscaling around the model-server process.

The endpoint contract includes input schema, model version, timeouts, concurrency, and error behavior as well as a URL. Canary or A/B delivery is useful only when requests and evaluation metrics can be associated with the version that produced each response.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

