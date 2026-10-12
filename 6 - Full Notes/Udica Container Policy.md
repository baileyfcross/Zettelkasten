2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Udica Container Policy

An Udica container policy is a workload-specific SELinux policy generated from a container inspection. Udica analyzes mounts, ports, capabilities, and other configuration, combines reusable Common Intermediate Language templates, and produces rules that grant the observed requirements without abandoning SELinux confinement.

The generated policy should be reviewed, versioned, and tested like other security configuration because the inspected container state determines its allowances. It is most valuable when a legitimate workload needs access beyond the default [[SELinux Container Type]] policy and hand-authoring the complete rule set would be error-prone.

# References

[[podmanfordevopssecondedition.pdf]]
