2026-10-31 12:52

Status: #baby

Tags: [[Selenium WebDriver and Browser Sessions]]

# WebDriver Page Loading

WebDriver page loading navigates the active session to an address with `get()`. The address can be an HTTP or HTTPS URL or a local `file:///` URL, allowing the same browser-control mechanism to open hosted or local content.

Loading establishes the document against which locators and interactions operate. HTTPS should be used where sensitive data is transmitted, while [[Offline Web Page Testing]] is useful for isolated static examples that do not require a server.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
