2026-11-11 18:27

Status: #baby

Tags: [[Application Debugging]]

# Minimal Debugging Change

A minimal debugging change fixes one identified defect before unrelated cleanup or a second repair is attempted. Keeping the change narrow allows the next test result to provide evidence about that specific causal hypothesis.

When several fixes and refactorings are mixed, a passing result does not reveal which change mattered and a new failure has several possible sources. After the first fix is verified and integrated, nearby defects or structural improvements can be handled as separate changes.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

