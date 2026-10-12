2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Conductive Waveguide Wall Model

A conductive waveguide wall model separates the hollow propagation domain from the metal surfaces that confine it. The interior receives dielectric properties, while the walls receive electrical conductivity and an [[Electromagnetic Impedance Boundary Condition]].

In the book, the interior is modeled as vacuum and the walls as very thin lossy conductive sheets, with a conductivity parameter of $6.3\times10^7$ S/m. The end faces are excluded from this wall selection because they serve as the two numeric ports.

Finite conductivity allows wall loss to be represented instead of assuming that every boundary is a perfect conductor. Its physical significance increases when the field penetrates a nonzero [[Electromagnetic Skin Depth]] into the material.

# References

[[rfmodule.pdf]]
