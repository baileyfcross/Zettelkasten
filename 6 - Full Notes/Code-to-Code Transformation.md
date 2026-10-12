2026-09-30 17:53

Status: #baby

Tags: [[Code LLM Development Workflows]]

# Code-to-Code Transformation

Code-to-code transformation takes code as input and produces code as output for completion, translation, repair, infilling, refactoring, or search. The output must preserve or deliberately modify semantics while satisfying the target language and repository conventions.

Small local transformations fit limited context more easily than project-wide changes. Translation or repair across modules needs dependency awareness, tests, and [[Generated Patch Validation]] because syntactic plausibility does not prove equivalent behavior.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
