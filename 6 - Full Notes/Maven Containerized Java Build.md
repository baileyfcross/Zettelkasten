2026-10-30 17:24

Status: #baby

Tags: [[Docker Image Engineering]]

# Maven Containerized Java Build

A Maven containerized Java build runs Maven and a selected JDK inside a disposable build container while mounting the project source and an output location. The host does not need the same Maven installation or Java toolchain as the build.

The build container is distinct from the application runtime image. Keeping compilation dependencies in the build environment prevents the final service artifact from inheriting an unnecessarily large development toolchain.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

