2026-10-31 12:52

Status: #baby

Tags: [[Selenium Frames and Synchronization]]

# Selenium Iframe Switch by Index

Selenium can switch to an iframe by its zero-based position among the frames in the current context. The first frame is index zero, the second is one, and an index with no corresponding frame raises a no-such-frame failure.

Index selection is useful when a frame has no stable identifier, but reordering or inserting frames changes its meaning. Returning to the main document is necessary before selecting a sibling frame from that document.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
