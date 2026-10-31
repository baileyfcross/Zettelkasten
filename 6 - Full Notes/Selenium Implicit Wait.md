2026-10-31 12:52

Status: #baby

Tags: [[Selenium Frames and Synchronization]]

# Selenium Implicit Wait

A Selenium implicit wait applies a global element-search timeout to the lifetime of a WebDriver instance. When a lookup cannot immediately find an element in the DOM, the driver polls until the element appears or the timeout expires.

Its simplicity comes with broad scope: every lookup inherits the same policy, which can introduce unintended delays and cannot express conditions such as clickability or text. The book recommends minimizing it in favor of targeted waits.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
