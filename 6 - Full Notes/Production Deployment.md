2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Production Deployment

A production deployment makes a selected application version available in the live environment. In a slot-based Azure flow, promotion can swap a verified staging version into the production role rather than copying unrelated files by hand.

The step should retain the artifact's version identity and use production-owned settings. Its success criteria include both deployment completion and evidence that the application operates at its live boundary.

# References

[[aspnetcore3andreact.pdf]]
