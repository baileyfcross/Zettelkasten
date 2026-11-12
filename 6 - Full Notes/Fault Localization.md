2026-11-11 18:27

Status: #baby

Tags: [[Application Debugging]]

# Fault Localization

Fault localization narrows a failure from its visible output to the statement, data transition, or interaction that first becomes incorrect. Reading the relevant code, tracing backward from the last correct observation, simplifying the input, and inspecting state at selected points all reduce the search region.

A debugger can stop execution, step through calls, and expose variables, but it does not replace understanding the surrounding design. Following one execution too closely can create tunnel vision, so the observed state must still be compared with the intended algorithm and requirements.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

