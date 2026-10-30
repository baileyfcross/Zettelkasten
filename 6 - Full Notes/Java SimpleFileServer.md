2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java SimpleFileServer

`SimpleFileServer` exposes the JDK's simple HTTP file-serving capability through Java code. A program selects a socket address, root path, and output level, creates an `HttpServer`, and controls when the server starts and stops.

The API can also supply a file handler for composition with a simple server. It remains designed for testing and development rather than as a secure production framework; unsupported methods and missing resources receive basic HTTP responses rather than application-specific behavior.

The programmatic API belongs to the `jdk.httpserver` module rather than the automatically resolved `java.base` module. Code that uses it therefore needs the module available explicitly, even though the command-line `jwebserver` wrapper hides most of that setup.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
