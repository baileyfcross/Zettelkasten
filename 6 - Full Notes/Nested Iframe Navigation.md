2026-10-31 12:52

Status: #baby

Tags: [[Selenium Frames and Synchronization]]

# Nested Iframe Navigation

Nested iframe navigation follows the frame hierarchy one level at a time. To reach a frame embedded inside another frame, Selenium first switches from the main document to the outer frame and then locates and switches to the inner frame.

A nested frame cannot be selected directly from an unrelated context. The active context determines which frames and elements are visible to the locator API.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
