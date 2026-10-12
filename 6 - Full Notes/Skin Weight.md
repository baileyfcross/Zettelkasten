2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Skin Weight

A skin weight states how strongly one skeletal bone influences a mesh vertex. A vertex commonly stores several bone indices and nonnegative weights whose total is normalized to one.

Vertices near a joint blend neighboring bone transforms, producing a smoother bend than rigid attachment to one bone. The number of influences is limited so [[Vertex Skinning]] remains efficient and fits the vertex format.

# References

[[gameprogrammingincplusplus.pdf]]
