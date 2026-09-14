2026-09-14 01:58

Status: #baby

Tags: [[CSS Transforms Transitions and Animation]]

# CSS Transition Reversal

A transition reverses when the triggering state returns toward its baseline before or after the forward transition completes. CSS can begin a reverse transition from the property's current interpolated value rather than jumping to an endpoint.

When interrupted, the reverse duration can be shortened according to how far the first transition progressed. This preserves a consistent apparent rate instead of spending the full declared duration over a smaller remaining distance.

# References

[[css_thedefinitiveguide.pdf]]
