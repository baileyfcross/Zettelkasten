2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Pattern Dominance

Java pattern dominance determines whether an earlier switch label already matches every value that a later label could match. A general type pattern placed before a more specific pattern makes the later case unreachable, so modern Java reports the ordering as a compilation error.

Dominance reasoning mainly covers types and constants, not the full meaning of arbitrary [[Java Switch Pattern Guard]] conditions. Two guards on the same type can therefore compile in an order that makes the second ineffective; the source order still has to progress from specific conditions toward general fallbacks.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
