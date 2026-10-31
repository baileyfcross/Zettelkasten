2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Selenium Element State Exception

A Selenium element-state exception occurs when an element exists but cannot support the requested operation. Examples include a hidden or disabled control, an unselectable element, or a visible-looking target obstructed from interaction.

The test should first distinguish presence, visibility, enabled state, and selectability. A matching [[Selenium Expected Condition]] can synchronize with a legitimate transition; JavaScript should not be used merely to bypass behavior the user could not perform.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
