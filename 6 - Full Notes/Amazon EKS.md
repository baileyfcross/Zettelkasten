2026-09-27 18:58

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# Amazon EKS

Amazon Elastic Kubernetes Service provides a managed Kubernetes control plane for container workloads. It lets teams use Kubernetes APIs and ecosystem tools while AWS operates the highly available control-plane infrastructure.

Worker capacity, cluster access, network policy, images, application configuration, and upgrades still require planning. EKS is useful when Kubernetes compatibility and portability justify its operational complexity; it is not automatically simpler than a more AWS-specific container service.

The book separates the AWS-managed control plane from worker nodes created in the customer's account. The control-plane API is exposed through the cluster endpoint and connected into VPC subnets, while registered EC2 workers supply the capacity on which the example microservice pods run.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
