2026-10-30 16:54

Status: #baby

Tags: [[Java Release and Feature Lifecycle]]

# Java Incubator Feature

A Java incubator feature is a preliminary implementation delivered in a separate JDK module for experimentation and feedback. It is less settled than a [[Java Preview Feature]] and may change fundamentally or disappear before becoming a permanent platform facility.

Because an incubator module is not part of the default module graph, it must be added explicitly with `--add-modules` during compilation and execution. The Vector API illustrates this lifecycle: applications can test hardware-oriented capabilities while accepting that the API is not yet final.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
