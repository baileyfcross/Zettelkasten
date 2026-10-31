2026-10-31 12:52

Status: #baby

Tags: [[Selenium User Interaction Automation]]

# Selenium Checkbox Selection

Selenium checkbox selection treats each checkbox as an independent Boolean choice. A test locates controls by ID, label, name, value, or collection index, clicks only those whose current state differs from the desired state, and verifies the result with `isSelected()`.

A collection can be iterated to select or clear all options. Checking state before clicking prevents a supposedly idempotent setup step from accidentally toggling a control the wrong way.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
