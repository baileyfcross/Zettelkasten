2026-09-16 00:09

Status: #baby

Tags: [[Data Quality and Missing Data]] · [[R Data Transformation and Reshaping]]

# Character-to-Factor Conversion

Character-to-factor conversion represents a finite set of text categories as explicit levels. The conversion helps summaries and models treat the field as categorical rather than as arbitrary strings.

Analysts should normalize spelling and whitespace first, because accidental variants become distinct levels and can fragment the data.

The primer also distinguishes conversion in the opposite direction: factor-to-numeric conversion should normally pass through the level labels rather than use the internal integer codes. That precaution preserves the displayed numeric meaning instead of silently substituting category positions.

# References

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
