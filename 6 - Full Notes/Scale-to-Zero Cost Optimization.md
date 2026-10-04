2026-10-03 22:25

Status: #baby

Tags: [[Platform FinOps and Cost Management]]

# Scale-to-Zero Cost Optimization

Scale-to-zero cost optimization stops a workload when it has no current demand and recreates capacity when work returns. It fits development systems, scheduled internal services, batch jobs, and event-driven applications whose availability requirements do not justify continuous idle resources.

The savings must be weighed against startup latency, state preservation, dependency availability, and the reliability of the trigger that restores service. Virtual-machine schedules, serverless platforms, and Kubernetes event-driven autoscaling implement the pattern at different layers. A self-service request can capture the hours or duration needed so shutdown becomes part of the resource contract rather than a later cleanup project.

# References

[[platformengineeringforarchitects.pdf]]
