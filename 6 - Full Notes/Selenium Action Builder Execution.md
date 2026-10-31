2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Action Builder Execution

Selenium action builder execution uses `perform()` to send the sequence accumulated by an `Actions` object. Movement, key presses, pauses, and releases can be composed first and executed as one ordered interaction.

After one sequence, `reset()` clears the builder's current input state so a new sequence can be assembled without constructing another builder. Resetting the builder does not reverse actions already performed in the browser.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
