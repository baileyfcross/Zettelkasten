2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# CSSOM-Dependent Image Loading

A browser generally needs the stylesheet and enough style resolution to know whether a CSS background rule applies. Media queries, selector matching, and overridden declarations can therefore determine whether and when a background URL is requested.

This behavior differs from an HTML image URL that a speculative scanner can see immediately. Placing critical content only in CSS may delay discovery, while CSS can avoid loading decorative assets for nonmatching conditions. See [[CSS Background Image Request Discovery]].

# References

[[highperformanceimages.pdf]]
