2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Script Execution Order

Unity script execution order controls which classes receive a lifecycle phase before or after the default group. It can resolve a dependency when one script must establish state before another reads it during the same frame.

An ordering setting should document a real invariant, not conceal uncontrolled coupling. If correctness depends on timing that is invisible from the code, later changes can reintroduce order-sensitive failures. Direct initialization, explicit events, or a coordinating object are often clearer, while execution order remains useful when engine callbacks must be sequenced.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

