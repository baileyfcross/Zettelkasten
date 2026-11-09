2026-11-08 14:08

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Testcontainers Integration Testing

Testcontainers starts disposable containerized dependencies or applications inside an integration test. A test can launch a database container, a Docker Compose environment, or both, discover the exposed host and port, and then call the running application's REST boundary with an ordinary client.

Using the same container images as deployment narrows environmental differences while keeping each run isolated and repeatable. This form of test is slower than a unit test because it exercises real runtime components and persistence, but it can verify multi-step behavior, configuration, serialization, network calls, and database state that mocks do not establish.

The Spring Boot source favors real MongoDB, Redis, CockroachDB, Kafka, and RabbitMQ containers over unlike embedded substitutes. A service connection can derive application properties from the container automatically, while dynamic property registration handles unsupported cases. The same infrastructure can launch a developer instance of the application against disposable services as well as support automated tests.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
