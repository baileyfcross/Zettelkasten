2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Responsible AI Controls]]

# Guardrail False Positive Calibration

Guardrail false positive calibration adjusts a safety control so legitimate requests are not blocked at an unacceptable rate. It requires a dataset of valid near-boundary examples as well as unsafe examples, because measuring only successful blocking rewards controls that reject too much.

Calibration combines threshold changes, narrower blocklist terms, improved context, revised prompts, and better refusal or recovery behavior. The correct balance depends on the severity of a missed harmful case and the cost of denying a valid user. Results should be recorded by category and population so aggregate rates do not conceal uneven impact.

# References

[[microsoftfoundryinaction.pdf]]
