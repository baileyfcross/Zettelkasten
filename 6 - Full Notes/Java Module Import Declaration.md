2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Module Import Declaration

A Java module import declaration makes the public types from every package exported by a named module available to one source file. One declaration can replace many package or type imports when a program broadly uses a module's API.

The declaration affects source-name availability rather than module readability or exports themselves. It can make compact examples easier to write, but the origin of a simple type name becomes less obvious and collisions require explicit resolution through [[Java Module Import Ambiguity]].

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
