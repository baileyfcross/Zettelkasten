2026-10-07 17:18

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Procedural Programming

Procedural programming decomposes a problem into functions or subroutines that perform identifiable steps of a larger algorithm. Arguments carry required information into a procedure, and functions commonly return the information produced by their work.

Procedures encourage reuse and make an algorithm's stages explicit. Their boundaries should also control data access: unrestricted global state lets one procedure alter information on which another silently depends, weakening the decomposition.

The software-design source distinguishes procedure boundaries chosen by control flow from modules chosen to hide changeable representations. A procedural solution can use both: subroutines express the algorithm's steps, while module interfaces prevent every step from depending on the same internal data decisions.

# References

[[statisticalcomputingincplusplusandr.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
