2026-10-31 12:52

Status: #baby

Tags: [[Selenium WebDriver and Browser Sessions]]

# WebDriver Browser Session

A WebDriver browser session is the controlled lifetime that begins when a browser-specific driver is instantiated. Commands such as loading a page, locating an element, changing a window, and reading state operate against that session.

Session ownership matters because windows, history, and element references belong to it. Cleanup should deliberately choose between [[WebDriver Close vs Quit|closing one active window and terminating the entire session]].

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
