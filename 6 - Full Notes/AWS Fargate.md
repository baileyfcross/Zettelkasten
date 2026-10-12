2026-09-27 20:01

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# AWS Fargate

AWS Fargate supplies serverless compute capacity for containers orchestrated by Amazon ECS or Amazon EKS. A team specifies container images, CPU, memory, networking, and task or pod behavior while AWS provisions and maintains the underlying hosts. Fargate removes node-fleet administration and supports per-workload isolation, but container startup, resource sizing, platform constraints, observability, and continuous usage cost still shape whether it fits a workload.

As a managed container execution option, Fargate trades host-level control for reduced node operations. Teams still own image security, workload identity, network exposure, resource requests, application resilience, and telemetry; “serverless” moves infrastructure responsibility rather than removing operational design.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]

