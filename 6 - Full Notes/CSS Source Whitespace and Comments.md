2026-09-14 01:58

Status: #baby

Tags: [[CSS Stylesheet Integration]]

# CSS Source Whitespace and Comments

CSS generally treats runs of source whitespace as equivalent where whitespace is permitted, so rules may be formatted over several lines for readability. Whitespace can still be required to separate tokens and can be significant inside quoted strings or certain expressions.

Comments use `/*` and `*/` delimiters and are removed during parsing. They document the stylesheet but do not nest, so an apparent inner closing delimiter ends the comment.

# References

[[css_thedefinitiveguide.pdf]]
