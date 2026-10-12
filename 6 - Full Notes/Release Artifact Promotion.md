2026-09-27 11:48

Status: #baby

Tags: [[Continuous Delivery Risk and Release Governance]]

# Release Artifact Promotion

Release artifact promotion moves the same versioned build output from one deployment stage to the next. The practice preserves the identity of what was tested and avoids introducing unverified differences through a later rebuild.

Environment-specific settings should be supplied at deployment rather than baked into separate binaries. Provenance then connects the production artifact back to its source revision, build, tests, and approvals.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
