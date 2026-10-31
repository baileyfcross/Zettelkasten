2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Drag and Drop

Selenium drag and drop moves a source element while the primary pointer button is held and releases it over a destination. `dragAndDrop(source, target)` expresses the element-to-element form, while `dragAndDropBy` moves the source by calculated offsets.

The operation can also be assembled from [[Selenium Pointer Button State|click-and-hold, movement, and release]]. A useful test validates the post-drop state, such as the source changing container or appearance.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
