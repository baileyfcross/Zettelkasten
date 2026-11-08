2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# Jakarta EE Profiles

Jakarta EE organizes its specifications into Platform, Web Profile, and Core Profile groupings. The Platform supplies the complete standardized enterprise application environment, while the Web Profile selects technologies aimed at web applications.

The Core Profile is the smaller cloud-oriented grouping. Profiles let a runtime claim a defined subset rather than treating all Jakarta specifications as inseparable, which is important for compact microservice runtimes such as [[Helidon MP Programming Model]].

The profiles form progressively broader standardized capability sets rather than competing editions of the same application. Core supplies a compact foundation, Web adds the technologies expected for web applications, and the full Platform covers the wider enterprise environment. An application can therefore select a compatible runtime according to the profile its required APIs actually inhabit.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
