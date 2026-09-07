2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Production Slot

A production slot is the deployment slot receiving the application's live traffic. Its address, settings, and backing services form the environment against which users exercise the released application.

A slot swap can promote a verified staging deployment into this role. Production-specific connection strings and secrets should remain associated with the live environment rather than being embedded in the artifact.

# References

[[aspnetcore3andreact.pdf]]
