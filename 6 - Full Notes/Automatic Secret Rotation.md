2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Automatic Secret Rotation

Automatic secret rotation replaces a stored credential on a schedule or in response to an event, updates the authoritative secret store, and coordinates consumers so the old value can be retired. Automation narrows the lifetime of a compromised credential without depending on a person to remember every rotation.

Reliable rotation needs a transition strategy because producers and consumers may not update at exactly the same moment. Versioned values, health checks, rollback, and audit logs make the change observable. Where supported, a [[Dynamic Secret]] can avoid repeated distribution of a long-lived value altogether.

# References

[[clouddevopsengineersguide.pdf]]
