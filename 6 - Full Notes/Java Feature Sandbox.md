2026-10-30 16:54

Status: #baby

Tags: [[Java Release and Feature Lifecycle]]

# Java Feature Sandbox

A Java feature sandbox is a small isolated project or execution environment used to try a new language or platform feature without coupling the experiment to a production application. It keeps compiler flags, JDK versions, and minimal examples visible while making failures inexpensive.

The book uses [[JShell Interactive Evaluation]], command-line source launching, and a dedicated sandbox module as complementary options. JShell favors immediate statements, direct launch favors a small source file, and a sandbox project is better when the experiment needs packages, dependencies, or IDE support.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
