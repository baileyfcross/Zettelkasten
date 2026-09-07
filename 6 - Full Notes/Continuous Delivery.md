2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]], [[Continuous Integration and Delivery]]

# Continuous Delivery

Continuous delivery keeps the game in a deployable state and makes releases frequent, routine decisions. Automated building, testing, configuration, and deployment preparation reduce the risk and transaction cost of each release.

Delivery does not mean every verified change is automatically exposed to players. It ensures that the team can choose to deploy without a separate destabilizing integration phase.

In the book's Azure flow, versioned build artifacts enter a release pipeline and are deployed to a staging environment before production promotion. Environment configuration stays outside the artifact, allowing the same tested package to remain ready for a deliberate release decision.

# References

[[agilegamedevelopment2e.pdf]]
[[aspnetcore3andreact.pdf]]
