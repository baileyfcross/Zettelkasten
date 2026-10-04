2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]]

# Build Context

A build context is the directory tree made available to a container image build. `COPY` and `ADD` resolve their source paths within this boundary, so choosing the context determines which application files can enter the build and how much data the builder must examine or transfer.

The context should be narrow and filtered because local artifacts, credentials, and unrelated directories can otherwise become available to an instruction or invalidate useful caches. A Dockerfile or [[Containerfile]] describes the build, but the context supplies its local inputs; reproducibility depends on controlling both.

# References

[[podmanfordevopssecondedition.pdf]]
