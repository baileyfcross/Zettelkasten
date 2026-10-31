2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Broken Image Validation

Selenium broken-image validation collects image elements, reads each `src` URL, and sends an HTTP request to check the response. A successful status indicates that the resource is accessible, while a not-found response identifies a broken image URL.

The check protects the visual integrity of pages and image-backed links. It validates resource availability; layout, alternative text, and the correctness of the displayed image require separate assertions.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
