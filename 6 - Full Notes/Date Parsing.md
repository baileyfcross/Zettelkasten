2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]] · [[Data Quality and Missing Data]] · [[R Data Transformation and Reshaping]]

# Date Parsing

Date parsing converts a character or factor representation into a date class by specifying the order and format of its components. Month names, numeric months, two- or four-digit years, weekday text, and separators all require matching format codes.

A value that looks like a date on screen may still be text internally. Parsing should therefore be followed by a class check and sample comparison, because a mistaken format can produce missing or misinterpreted dates that contaminate every later time calculation.

In the book's wrangling pattern, corrected dates become the basis for [[Derived Temporal Feature|derived year and season features]]. Parsing must precede that derivation so apparently valid text does not produce misleading calendar groups.

R distinguishes calendar dates from date-time values and uses format directives to interpret and display components such as year, month, day, hour, minute, and second. Parsing and formatting are inverse-looking operations but serve different purposes: one constructs the temporal object, while the other controls its textual representation.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
