2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Qualified Enum Constant in switch

Modern Java permits a switch label to name an enum constant with its enum type, such as `Direction.NORTH`. Qualification matters when a switch operates on a common supertype and must distinguish constants drawn from several enum implementations.

Constants from different enum subtypes can then share one switch while retaining clear origins and participating in completeness analysis. Static imports may shorten the final form, but explicit qualification is useful when identical constant names would otherwise be ambiguous.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
