2026-10-11 12:45

Status: #baby

Tags: [[Sentiment Analysis Methods]]

# Rating-Derived Sentiment Label

A rating-derived sentiment label converts a review’s star score into a positive or negative class for supervised learning. It supplies many inexpensive labels without requiring a reader to annotate every review.

The label is a proxy: the written text may be mixed, sarcastic, or inconsistent with the score, and middle ratings may not map cleanly to either class. Models trained this way learn the relationship between language and the rating rule, so the threshold and excluded ratings must be documented.

# References

[[textminingandvisualization.pdf]]
