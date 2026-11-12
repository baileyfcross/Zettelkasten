2026-11-11 18:27

Status: #baby

Tags: [[Application Debugging]]

# Root Cause Debugging

Root cause debugging repairs the rule or state transition that generated a failure rather than adding code that hides its current symptom. A special-case guard may make one input pass while preserving the same flawed assumption for the next edge case.

The proposed cause should explain the evidence: why the failure appears under the reproduced conditions, why nearby cases behave differently, and why the correction restores the intended invariant. That explanation makes the fix reviewable instead of merely hopeful.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

