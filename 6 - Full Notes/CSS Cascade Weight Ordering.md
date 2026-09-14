2026-09-14 01:58

Status: #baby

Tags: [[CSS Cascade and Inheritance]]

# CSS Cascade Weight Ordering

Cascade weight separates important declarations from normal declarations before selector strength is considered. In the order described by the source, reader important declarations outrank author important declarations, followed by author normal, reader normal, and user-agent declarations.

This stage explains why a more specific normal selector can still lose to a less specific important declaration. Only declarations in the same weight-and-origin group proceed to [[CSS Cascade Specificity Ordering]].

# References

[[css_thedefinitiveguide.pdf]]
