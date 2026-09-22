2026-09-05 15:58

Status: #baby

Tags: [[Agile Engineering and Quality]] [[Web Application Testing]]

# Test-Driven Development

Test-driven development creates an automated test before the functionality that will satisfy it, then implements the smallest behavior needed and improves the design under the test's protection. The test makes the intended behavior explicit before code structure dominates the decision.

The growing suite becomes a safety net for refactoring and change. TDD is most applicable to behavior that can be expressed reliably in automated checks.

ASP.NET Core and Angular tests apply the same cycle with different tools: xUnit.net and Moq isolate back-end behavior, while Jasmine, Karma, and TestBed exercise front-end components. [[Behavior-Driven Development]] provides a related emphasis on describing observable behavior.

The inventory project uses tests around commands, factories, and the shared repository to make expected behavior visible while the design changes. In particular, tests expose a race in concurrent quantity updates and a lifetime error when each resolution builds a new dependency-injection provider. Passing tests measure the implemented behavior, not the completeness of user acceptance testing.

# References

[[agilegamedevelopment2e.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
