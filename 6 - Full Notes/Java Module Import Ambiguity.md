2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Module Import Ambiguity

A Java module import can expose two public types with the same simple name from different exported packages or modules. The compiler cannot choose the intended type from that simple name and reports an ambiguity instead of depending on an arbitrary import order.

The source can resolve the conflict with a specific single-type import or a fully qualified name. This tradeoff is the main cost of the concise [[Java Module Import Declaration]]: broad visibility shortens the import section but may require local precision at collisions.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
