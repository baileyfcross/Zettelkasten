2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]]

# Binary Outcome Variable

A binary outcome variable encodes whether an event or condition is present, usually with 1 for the event and 0 for its absence. This representation is used directly by [[Logistic Regression]] and can also serve as the event indicator in time-to-event analysis.

Special responses such as refused, uncertain, or missing should not be silently converted into absence. The source categories must first be validated, then recoded so every retained observation has an unambiguous outcome state.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
