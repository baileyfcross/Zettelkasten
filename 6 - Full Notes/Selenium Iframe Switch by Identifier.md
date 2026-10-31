2026-10-31 12:52

Status: #baby

Tags: [[Selenium Frames and Synchronization]]

# Selenium Iframe Switch by Identifier

Selenium can switch to an iframe using its stable ID or name. `switchTo().frame()` accepts the identifier and makes that embedded document the active [[Selenium Iframe Browsing Context]].

After the switch, locators operate only inside the frame until another context change occurs. An identifier is generally clearer and more stable than an index when the page supplies one.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
