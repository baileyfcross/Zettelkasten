2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]]

# Variable Class

A variable class describes how statistical software interprets a column, such as numeric, integer, character, factor, or date. The same visible values can behave differently in summaries and models depending on their class.

Class must reflect analytic meaning. A coded category stored as a number may otherwise be treated as continuous, while a date stored as text cannot participate correctly in date arithmetic. Checking and deliberately converting classes prevents these implicit modeling errors.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
