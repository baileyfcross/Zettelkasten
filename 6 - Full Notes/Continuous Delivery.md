2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]], [[Continuous Integration and Delivery]]

# Continuous Delivery

Continuous delivery keeps the game in a deployable state and makes releases frequent, routine decisions. Automated building, testing, configuration, and deployment preparation reduce the risk and transaction cost of each release.

Delivery does not mean every verified change is automatically exposed to players. It ensures that the team can choose to deploy without a separate destabilizing integration phase.

In the book's Azure flow, versioned build artifacts enter a release pipeline and are deployed to a staging environment before production promotion. Environment configuration stays outside the artifact, allowing the same tested package to remain ready for a deliberate release decision.

The design-patterns source describes development, user-acceptance testing, and production as distinct promotion boundaries. Builds and checks can be automated while production still requires a scheduled or approved release, preserving a deployable artifact without claiming every passing change is live.

The source extends successful integration into a multistage path where a versioned artifact can be promoted through test and staging toward production. Delivery means the release is ready and repeatable even when final production approval remains manual.

A cloud delivery pipeline preserves the same tested artifact while changing the controls around promotion. Infrastructure plans, security scans, environment checks, and a [[Manual Deployment Approval]] can sit between build and production without turning the release into a manually reconstructed procedure. The deployable state is maintained continuously even when the business chooses the release time.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[agilegamedevelopment2e.pdf]]
[[aspnetcore3andreact.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
[[clouddevopsengineersguide.pdf]]
