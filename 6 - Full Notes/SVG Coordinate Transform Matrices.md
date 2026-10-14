2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Coordinate Transform Matrices

SVG transformations change the coordinate system in which geometry is interpreted. Translation moves the origin, scaling changes unit size, rotation changes axis direction, and skew makes one coordinate depend on the other. Their order matters because scaling a translated system is generally different from translating a scaled system.

Each two-dimensional transform can be represented as an affine matrix. Multiplying matrices combines a transform list, ancestor transforms, and implicit viewBox mapping into one cumulative transform that maps a point from local [[SVG Coordinate Grid|user space]] to another reference frame. The compact six-parameter SVG matrix is therefore not a separate kind of visual effect; it is the consolidated form of familiar transform operations.

Matrix composition is also what makes inverse mapping possible. Interactive code can obtain the cumulative screen transform, invert it, and map a browser pointer position back into local SVG coordinates, as described in [[SVG Pointer Coordinate Conversion]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

