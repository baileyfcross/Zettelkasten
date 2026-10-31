2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Effective Final Capture

A local or anonymous class may capture a local variable or parameter from its enclosing block only when that value is final or effectively final. An effectively final variable is assigned once and never changed afterward even though its declaration omits the `final` modifier.

Attempting to assign another value or increment the captured variable breaks that condition and is rejected. The nested object can still use the captured value after the enclosing method returns because the capture records the value needed by the class instance.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
