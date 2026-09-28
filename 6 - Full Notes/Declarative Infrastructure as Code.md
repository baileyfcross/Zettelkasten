2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Declarative Infrastructure as Code

Declarative Infrastructure as Code describes the desired end state of infrastructure and leaves the tool to determine the operations required to reach it. This differs from an imperative script that specifies a sequence such as creating a server, attaching a disk, and installing software.

Terraform applies the declarative model by comparing configuration with recorded and live state. The same definition may cause creation on the first run, modification after a property changes, or deletion after a resource is removed. The stable object of review is therefore the desired state, while the execution sequence is derived from the current difference.

# References

[[clouddevopsengineersguide.pdf]]

