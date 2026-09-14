2026-09-14 01:58

Status: #baby

Tags: [[CSS Cascade and Inheritance]]

# CSS Source Order Tie-Breaking

Source order is the final CSS cascade comparison for declarations with equal importance, origin, and specificity. The declaration encountered later wins the contested property.

Imported and linked stylesheets participate in an overall order determined by where they enter the document's style sources. Source order makes deliberate overrides possible, but it acts only after [[CSS Cascade Weight Ordering]] and [[CSS Cascade Specificity Ordering]].

# References

[[css_thedefinitiveguide.pdf]]
