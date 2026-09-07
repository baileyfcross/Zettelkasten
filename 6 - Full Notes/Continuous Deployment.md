2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]], [[Continuous Integration and Delivery]]

# Continuous Deployment

Continuous deployment automatically releases every change that passes the delivery pipeline to the live environment. It extends [[Continuous Delivery]] by removing the manual release decision from the normal flow.

Because games can have platform, player, and experiential constraints, teams may use staged exposure or feature toggles instead. The principle is to make deployment small, repeatable, observable, and reversible.

An Azure DevOps pipeline can remove routine manual execution by triggering a build, publishing an artifact, and advancing automated deployment stages when their checks pass. Whether production promotion is automatic determines whether this is continuous deployment rather than continuous delivery.

# References

[[agilegamedevelopment2e.pdf]]
[[aspnetcore3andreact.pdf]]
