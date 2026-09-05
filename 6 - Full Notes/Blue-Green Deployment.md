2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]]

# Blue-Green Deployment

Blue-green deployment maintains two equivalent production environments: one serves the current version while the other receives and verifies the new version. Traffic switches only when the new environment is ready.

The previous environment provides a rapid rollback path if the release fails. The technique reduces transition risk but requires duplicated capacity and careful management of shared data changes.

# References

[[agilegamedevelopment2e.pdf]]
