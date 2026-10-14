2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Intersection Observer for Image Loading

Intersection Observer lets code receive asynchronous notifications when an element crosses a visibility threshold relative to a viewport or another root. It avoids repeatedly calculating positions during every scroll event.

A lazy loader can keep the real image URL out of the native loading attribute, observe the placeholder, and restore the URL when the element approaches view. The observer improves scheduling mechanics, but the implementation still needs fallbacks and must exempt critical images. See [[No-JavaScript Lazy-Load Fallback]].

# References

[[highperformanceimages.pdf]]
