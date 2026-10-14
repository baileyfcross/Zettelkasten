2026-10-11 12:45

Status: #baby

Tags: [[Text Feature Representation]]

# Text Stemming

Text stemming maps related inflected words to a shared reduced form before features are counted. Treating forms such as “stem,” “stemmed,” and “stemming” alike can shrink a vocabulary and combine evidence that would otherwise occupy separate columns.

The reduction is mechanical rather than semantic, so a stem may be hard to read or may merge forms whose meanings differ in context. Stemming is therefore a configurable preprocessing choice whose value should be tested with the downstream model rather than assumed.

# References

[[textminingandvisualization.pdf]]
