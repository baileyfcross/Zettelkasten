2026-10-11 21:26

Status: #baby

Tags: [[Docker Container Security]]

# Build-Time Container Secret

A build-time container secret gives a build step temporary access to a credential needed for a private dependency or registry without copying that value into a Dockerfile instruction, build argument, environment layer, or final filesystem. The secret is mounted only for the authorized BuildKit operation.

The build must avoid writing the value into package configuration, shell history, caches, or copied artifacts before the step completes. Multi-stage separation helps keep build tools and intermediate state out of the runtime image, but it does not erase a secret deliberately persisted in a layer.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
