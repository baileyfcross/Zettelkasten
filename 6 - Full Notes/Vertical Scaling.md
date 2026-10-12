2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]] [[Software Quality Attributes and Architecture Tradeoffs]]

# Vertical Scaling

Vertical scaling increases or decreases the capacity of one running system by changing resources such as CPU, memory, or storage. A cloud host can move an application to a larger service tier without changing how many instances exist. This can relieve a bottleneck quickly, but one instance retains an upper size limit and may remain a single failure point.

The approach usually requires fewer application changes than distributing work across replicas, making it a useful first tradeoff when its capacity ceiling and interruption behavior remain acceptable.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
