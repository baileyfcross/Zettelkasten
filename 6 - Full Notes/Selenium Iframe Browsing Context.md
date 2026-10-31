2026-10-31 12:52

Status: #baby

Tags: [[Selenium Frames and Synchronization]]

# Selenium Iframe Browsing Context

An iframe embeds a separate HTML document inside a page and therefore creates a separate browsing context. Elements inside it are not immediately addressable from the main document's context even when they are visibly displayed inside the same window.

Selenium must switch into the iframe before locating its contents and later return to a parent or the main document. This isolation is why ordinary element locators fail until the correct context is active.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
