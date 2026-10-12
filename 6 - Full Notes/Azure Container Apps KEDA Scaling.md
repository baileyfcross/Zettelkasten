2026-09-27 21:45

Status: #baby

Tags: [[Azure Container Platform Selection]]

# Azure Container Apps KEDA Scaling

Azure Container Apps uses Kubernetes Event-Driven Autoscaling to change replica count from HTTP demand or event sources such as Service Bus. A rule can scale a worker to zero when no messages exist and increase replicas as backlog grows. Scaling reacts to a signal rather than proving that processing is safe; concurrency, message locks, retries, idempotency, resource limits, and maximum replicas determine whether added instances improve throughput.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

