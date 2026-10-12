2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Build and Testing]]

# Automake Build Specification

Automake converts concise Makefile.am specifications into standard Makefile.in templates. ClusLib uses SUBDIRS to express build order, header variables to define installed interfaces, source variables to define compilation units, and library variables to combine subject libraries.

The generated makefiles provide conventional build, clean, install, and distribution targets. Recipe tabs and line-continuation syntax remain significant, so the specification must preserve make's textual rules.

# References

[[dataclusteringincplusplus.pdf]]

