2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Deferred Image Loading

Deferred loading postpones noncritical image requests until important page work has finished, then loads them even if they are still outside the viewport. It reduces early competition while preparing later content for smooth scrolling.

This differs from strict on-demand lazy loading, which may never fetch unseen images. Deferred loading spends more total bandwidth but lowers the chance that a user scrolls to an empty slot. The choice depends on whether early responsiveness or maximum transfer avoidance is the stronger goal.

# References

[[highperformanceimages.pdf]]
