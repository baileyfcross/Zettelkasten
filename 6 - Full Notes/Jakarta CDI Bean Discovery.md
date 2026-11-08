2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Bean Discovery

Jakarta CDI discovers managed components when an application starts. The beans.xml bean-discovery-mode setting controls the scan: all includes eligible classes even without bean-defining annotations, annotated limits discovery to classes with bean-defining annotations, and none disables discovery for that archive. Annotated is the default mode.

Discovery gives the container a model of the application's beans and their relationships before requests begin. The selected mode therefore affects both startup work and which classes can participate in injection; an unannotated class that is visible under all may not be a bean under annotated.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
