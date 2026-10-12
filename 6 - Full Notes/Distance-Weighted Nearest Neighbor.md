2026-09-14 21:00

Status: #baby

Tags: [[Rule and Instance-Based Classification]]

# Distance-Weighted Nearest Neighbor

Distance-weighted nearest neighbor gives closer training instances more influence on a test label than farther members of the selected neighborhood. A decreasing function of distance supplies each vote's weight.

Weighting softens the arbitrary boundary between the last included neighbor and the first excluded one. The method still depends on meaningful feature scaling because a distorted distance changes both neighborhood membership and voting strength.

# References

[[dataclassification.pdf]]
