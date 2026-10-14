2026-10-11 12:45

Status: #baby

Tags: [[Text Feature Representation]]

# Custom Stop List

A custom stop list adds corpus-specific high-frequency or irrelevant terms to a general list used by [[Stop-Word Removal]]. Names, headers, boilerplate, and collection artifacts may dominate counts even though they do not help answer the analytical question.

The list should be revised after inspecting frequent terms or model outputs. Removing a word changes every later frequency, vector, topic, and visualization, so a custom stop list is part of the analytical model rather than a neutral cleanup step.

# References

[[textminingandvisualization.pdf]]
