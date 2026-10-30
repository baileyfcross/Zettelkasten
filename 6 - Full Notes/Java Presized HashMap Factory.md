2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Presized HashMap Factory

Java's presized `HashMap` factory creates a map sized for an expected number of mappings rather than treating the supplied number as the raw backing capacity. It accounts for the load factor so the requested mappings can be inserted without an early resize.

With the default load factor of 0.75, a raw capacity of 1,000 does not hold 1,000 mappings before expansion. The factory expresses the caller's actual intent and calculates the larger internal capacity required by that load policy.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
