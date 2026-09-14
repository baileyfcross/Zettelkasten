2026-09-14 01:58

Status: #baby

Tags: [[CSS Web Typography]]

# CSS Font Source Descriptors

Within [[CSS Font Face Rule|`@font-face`]], the `src` descriptor provides an ordered list of possible font resources. A source can request a locally installed font or refer to a downloadable URL, optionally giving a format hint.

The browser works through the list until it finds a usable source. Other descriptors narrow the character range and the weight, style, or stretch represented by that resource so it can be matched correctly.

# References

[[css_thedefinitiveguide.pdf]]
