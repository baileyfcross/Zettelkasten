2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# TestNG Data Provider

A TestNG data provider supplies multiple argument sets to one test method. A method annotated with `@DataProvider` returns rows of values, and the test's `dataProvider` attribute connects those rows to its parameters.

TestNG invokes the test once for each row, enabling data-driven coverage without duplicating the scenario. Each data set should produce an identifiable result so a failure reveals which input combination was responsible.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
