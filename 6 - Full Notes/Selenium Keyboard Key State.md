2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Keyboard Key State

Selenium keyboard key state models pressing and releasing non-text keys inside an action chain. `keyDown()` holds a modifier such as Shift or Control, while `keyUp()` releases it after the dependent input. Selenium's `Keys` constants represent special and non-printable keys.

Explicit state makes combinations such as uppercase input or multi-selection reproducible. A modifier should be released before the sequence ends unless the intended interaction requires it to remain held.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
