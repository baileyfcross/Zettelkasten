2026-11-11 19:33

Status: #baby

Tags: [[Platform Delivery and Artifact Automation]]

# Maven Docker Image Build Plugin

A Maven Docker image build plugin makes container construction, tagging, and publication part of the Java build lifecycle. The Fabric8 plugin can describe a base image, assembled artifact, ports, environment, image name, and registry behavior in the POM, while Spotify's Dockerfile plugin drives a project-controlled [[Dockerfile]] from Maven.

Binding the image to the project version helps the application artifact and image receive consistent identities. Registry credentials should remain outside the versioned POM—for example, in Maven settings—so automating a push does not turn the build descriptor into a credential store.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
