2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Transitive Module Import

A Java module import also makes public types from transitively required modules available. Importing `java.sql`, for example, carries the exported public types of modules on which it transitively depends rather than forcing the source to repeat each module import.

The behavior mirrors the convenience of transitive library dependencies in a build tool, but at the source-import level. It reduces boilerplate while increasing the importance of recognizing which module ultimately contributes a type.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
