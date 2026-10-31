2026-10-31 13:15

Status: #baby

Tags: [[Java String Processing and Mutable Text]]

# Java Word Counting State Machine

A simple Java word counter can read one character at a time and retain a Boolean state recording whether the preceding character placed the scan inside a word. A nonalphabetic character clears that state; an alphabetic character encountered while outside a word starts one and increments the count.

The counter therefore records transitions into words rather than counting every alphabetic character. End-of-input terminates the loop, and the definition of alphabetic input determines which languages and character sets the counter recognizes.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
