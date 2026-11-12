2026-11-11 19:33

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker None Network

The Docker none network driver starts a container without attaching it to an external container network. The process remains separated from other containers and the outside network, making this mode useful when networking must be deliberately disabled.

Unlike a [[Docker Host Network]], which removes network isolation by sharing the host namespace, the none driver preserves an isolated networking boundary with no route for ordinary service communication.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
