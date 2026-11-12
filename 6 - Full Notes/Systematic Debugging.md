2026-11-11 18:27

Status: #baby

Tags: [[Application Debugging]]

# Systematic Debugging

Systematic debugging follows a repeatable sequence: reproduce the failure reliably, locate its source, repair that one defect, test the fix, and inspect nearby code for related defects. Each step narrows uncertainty rather than changing code on a guess.

The method distinguishes a symptom from its cause. Adding a special case that suppresses one visible failure can leave the underlying rule broken, whereas a general correction explains both the observed case and why similar inputs will now behave correctly.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

