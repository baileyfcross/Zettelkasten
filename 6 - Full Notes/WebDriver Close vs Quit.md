2026-10-31 12:52

Status: #baby

Tags: [[Selenium WebDriver and Browser Sessions]]

# WebDriver Close vs Quit

WebDriver `close()` and `quit()` end different scopes of browser activity. `close()` closes only the currently focused browser window or tab, leaving other windows in the same session available. `quit()` closes every window associated with the driver and terminates the entire session.

Selective closing is useful in multi-window flows. Test teardown normally uses `quit()` so the [[WebDriver Browser Session]] releases its resources and does not leave orphaned browser processes.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
