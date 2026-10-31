2026-10-30 17:24

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Inter-Microservice Consistency Gap

An inter-microservice consistency gap appears when one service commits its local change and a later service operation fails. The source's example reduces inventory successfully but then fails to create the booking, leaving two service-owned tables in conflicting states.

Because the services do not share one global transaction, a rollback cannot be assumed. The gap must be detected and corrected through the system's chosen recovery or reconciliation mechanism.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

