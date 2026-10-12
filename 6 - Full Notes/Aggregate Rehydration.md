2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Aggregate Rehydration

Aggregate rehydration reconstructs an [[Event-Sourced Aggregate]] by reading its historical [[Event Stream]] and applying each event in order. This is a fold: every event transforms the current state into the next state until the last known version is reached. Historical application must not add those events to the list of uncommitted changes. After rehydration, a new command can run against the current state and append only the newly produced events.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
