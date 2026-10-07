2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]], [[SLES Container and SAP Workload Operations]]

# Trusted Container Registry

A trusted container registry is an explicitly approved image source whose identity, transport, publishing controls, and content policies meet the consumer's requirements. Podman's registry configuration can prioritize known sources, qualify short names, configure mirrors, or block entire registries, namespaces, and images.

Registry trust and image trust are related but distinct. TLS and source configuration protect how a client reaches the service, while [[Container Image Signature]] verification can establish that particular content was signed by an accepted identity. An official-looking repository name alone supplies neither guarantee.

SLES container examples use SUSE's registry and SUSE base images, making exact registry names and image tags part of the provenance boundary. Short-name search configuration should not silently redirect an intended vendor image to an unrelated public namespace.

# References

[[podmanfordevopssecondedition.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
