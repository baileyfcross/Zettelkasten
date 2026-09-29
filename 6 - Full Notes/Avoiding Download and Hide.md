2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# Avoiding Download and Hide

A “download and hide” design loads a large or unwanted image and then suppresses it with CSS at certain breakpoints. The network cost has already been paid even though the pixels never appear.

Responsive source selection should prevent the unsuitable resource from being chosen in the first place. Conditional `picture` sources or deliberately empty alternatives can express the intended layout before download, while decorative CSS images can be placed behind nonmatching media rules. See [[CSSOM-Dependent Image Loading]].

# References

[[highperformanceimages.pdf]]
