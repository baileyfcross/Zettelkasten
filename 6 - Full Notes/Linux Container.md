2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Linux CPU Scheduling and Control Groups]]

# Linux Container

A Linux container runs an application against a Linux-oriented container image and runtime environment. The book chooses this target for its .NET Core 3 console worker even though development occurs on Windows.

Cross-platform .NET makes the managed application portable, but filenames, casing, native dependencies, and operating-system APIs still need to be compatible with Linux. Containerization makes that target environment testable before deployment.

At the Linux kernel level, namespaces isolate what containerized processes can see, while [[Linux Control Groups]] account for and constrain resources such as CPU time and memory. A container therefore combines several kernel mechanisms rather than representing a separate kernel or a single isolation primitive.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
