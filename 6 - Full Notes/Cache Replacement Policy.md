2026-09-22 23:34

Status: #baby

Tags: [[Distributed Network Caching Monitoring and Inspection]]

# Cache Replacement Policy

A cache replacement policy chooses which entry to remove when bounded cache capacity is needed for a new value. The decision can consider recency, frequency, cost, size, or an application-specific estimate of future reuse.

No single heuristic is optimal for every access pattern. The policy should reflect measured requests and avoid evicting expensive or frequently reused data merely because a simple ordering rule is convenient.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
