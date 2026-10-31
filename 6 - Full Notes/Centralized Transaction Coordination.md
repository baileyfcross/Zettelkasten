2026-10-30 17:24

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Centralized Transaction Coordination

Centralized transaction coordination gives one application process responsibility for deciding whether an end-to-end business transaction succeeds or fails. When participating modules and tables share one server and database context, a local ACID transaction can commit every change or roll them all back together.

The arrangement simplifies atomic consistency but concentrates control, deployment, and failure in the coordinating tier. Moving capabilities into independent services removes this implicit local transaction boundary and requires an explicit distributed consistency model.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

