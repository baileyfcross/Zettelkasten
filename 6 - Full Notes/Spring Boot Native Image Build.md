2026-11-11 19:33

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Boot Native Image Build

Spring Boot supports two GraalVM native-image build paths. Its [[Spring Boot Buildpack Image]] path uses Maven or Gradle to create a container containing the native executable and requires access to Docker during the build. The GraalVM native build tools instead compile a directly runnable executable with the native compiler installed in the build environment.

Most application tests can remain on the JVM for fast feedback, while AOT processing and native test tasks verify that compilation preserves the application's required behavior. Dynamic reflection, resources, proxies, serialization, or JNI paths that static analysis cannot discover may require a [[Spring Native Runtime Hint]].

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
