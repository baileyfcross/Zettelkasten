2026-10-30 17:24

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Microservice Functional Growth

Microservice functional growth adds behavior to one service type, making that service larger over time. It resembles vertical growth in architecture: the existing unit gains more responsibility instead of introducing a separate business capability.

Unbounded functional growth can recreate a monolith inside one deployment. The service's cohesion, release reasons, data ownership, and scaling needs should determine whether the new behavior belongs there or warrants a separate type.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

