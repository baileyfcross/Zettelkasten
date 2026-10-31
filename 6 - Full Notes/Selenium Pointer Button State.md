2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Pointer Button State

Selenium pointer button state can be held across several actions. `clickAndHold()` presses the primary button without releasing it, and `release()` ends that held state after movement or another step.

This separation is the basis of manual [[Selenium Drag and Drop|drag-and-drop sequences]]. Every held input should have a deliberate release so later actions do not inherit unintended pointer state.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
