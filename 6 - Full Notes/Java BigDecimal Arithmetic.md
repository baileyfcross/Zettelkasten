2026-10-31 13:15

Status: #baby

Tags: [[Java Numeric Utilities and Arbitrary Precision]]

# Java BigDecimal Arithmetic

Java `BigDecimal` represents an immutable signed decimal value with an arbitrary-precision unscaled integer and a scale that positions the decimal point. Constructing a value from its decimal string preserves the intended base-ten digits without first passing through binary floating-point representation.

Arithmetic methods such as `multiply` return new BigDecimal objects. `setScale` can produce a value with the required number of fractional digits and an explicit rounding mode, making the type suitable for currency calculations whose decimal precision and rounding rule must be visible.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
