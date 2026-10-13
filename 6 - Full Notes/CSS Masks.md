2026-09-14 01:58

Status: #baby

Tags: [[CSS Filters Blending Clipping and Masking]]

# CSS Masks

A CSS mask uses an image's alpha or luminance values to control the visibility of an element. Unlike the hard in-or-out boundary of [[CSS Clipping Paths]], a mask can produce gradual partial transparency.

Mask layers can be sourced, sized, positioned, repeated, clipped, and composited in ways resembling background layers. Mask mode chooses whether alpha or luminance supplies the masking value, and mask type influences SVG mask interpretation.

SVG emphasizes the pixel nature of this operation: the mask is rasterized, each mask pixel is converted to an opacity value, and that value reduces the corresponding pixel in the masked layer. This permits feathered boundaries and partial visibility that a vector clip cannot express. The mask's coordinate units and region also determine how its image is scaled and where the effect is clipped.

# References

[[css_thedefinitiveguide.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
