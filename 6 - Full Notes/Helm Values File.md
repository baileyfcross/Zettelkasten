2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Helm Values File

A Helm values file supplies configuration to the templates in a [[Helm Chart]]. Values can select an image tag, replica count, resource limits, or other supported settings without copying and directly editing every generated Kubernetes manifest.

Separate values files let one chart represent development, staging, and production variations. They should contain configuration appropriate for version control but not plaintext secrets. A values file is constrained by the chart's template interface; an environment difference that the chart does not expose cannot be made reliable by adding an unused key.

The book uses values to parameterize replica counts, images, resource names, ports, and database settings and to install one common application chart as several releases. Template expressions read the corresponding value paths, so the rendered manifest is the evidence that a supplied value actually participates in deployment.

# References

[[clouddevopsengineersguide.pdf]]

[[javamicroservicesandcontainersinthecloud.epub]]

