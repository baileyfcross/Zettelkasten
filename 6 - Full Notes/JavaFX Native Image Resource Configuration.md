2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# JavaFX Native Image Resource Configuration

Native-image analysis cannot always discover classes and assets reached through reflection, JNI, resource lookup, localization bundles, proxies, or serialization. GluonFX therefore exposes configuration lists for additional resource bundles, resources, reflective classes, and JNI classes beyond the defaults already known for JavaFX.

The native-image agent offers an evidence-driven alternative. A developer runs the application on GraalVM's desktop JVM and exercises its behavior while the agent records reflection, JNI, resource, proxy, and serialization use. The generated configuration then feeds the native build. This is most reliable when the recorded run covers every dynamic path needed in production. The same closed-world constraint affects [[GraalVM Native Image for JavaFX]] on desktop and [[GluonFX Mobile Compilation]] on mobile.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
