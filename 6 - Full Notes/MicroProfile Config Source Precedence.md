2026-11-08 14:08

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Config Source Precedence

MicroProfile Config can resolve one property key across several sources, using each source's ordinal to select the effective value. The built-in hierarchy gives Java system properties ordinal 400, environment variables 300, and META-INF/microprofile-config.properties 100; the value from the highest-ordinal source wins.

A custom ConfigSource can read another store and report its own ordinal. Sources with the same ordinal are ordered by source name. This precedence model lets a packaged application provide defaults while container or system configuration overrides them for an environment without changing code or rebuilding the artifact.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
