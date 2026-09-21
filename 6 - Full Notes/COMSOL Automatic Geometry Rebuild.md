2026-09-21 00:45

Status: #baby

Tags: [[COMSOL Geometry Configuration]]

# COMSOL Automatic Geometry Rebuild

COMSOL automatic geometry rebuild reruns dependent geometry features when an upstream parameter or operation changes. It keeps a parametric model synchronized and exposes whether later features remain valid under the new dimensions.

Automatic rebuilding accelerates exploration but can conceal cascading changes if results are not inspected. Stable selections, build messages, and measurement checkpoints are needed to confirm that a successful rebuild still represents the intended domains.

# References

[[geometrycreationandimport.pdf]]
