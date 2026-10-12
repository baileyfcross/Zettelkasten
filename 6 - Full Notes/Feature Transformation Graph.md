2026-09-16 01:38

Status: #baby

Tags: [[Automated Feature Engineering]]

# Feature Transformation Graph

A feature transformation graph represents datasets as nodes and transformation operations as directed edges. A child node contains features produced from its parent, while combination nodes can unite features from several paths.

The graph records derivation history and exposes shared intermediate results. Because repeated composition creates a vast directed acyclic graph, exploration must prioritize promising nodes instead of materializing every possibility.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
