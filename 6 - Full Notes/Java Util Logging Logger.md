2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Util Logging Logger

Java Util Logging is the JDK logging backend in `java.util.logging`. A named `Logger` creates records at methods corresponding to severity levels, and hierarchical logger names allow configuration to apply to a package or class family.

The backend can be configured without changing calling code by selecting levels, handlers, and formatters. Direct dependence on JUL ties the program to its API; a logging facade such as [[SLF4J Logging Facade]] adds another boundary when the implementation may need to change.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
