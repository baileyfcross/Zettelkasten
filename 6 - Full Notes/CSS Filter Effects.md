2026-09-14 01:58

Status: #baby

Tags: [[CSS Filters Blending Clipping and Masking]]

# CSS Filter Effects

The CSS `filter` property applies one or more visual operations to an element's rendered result. A value can use built-in filter functions or reference an external SVG filter, and a list applies operations in sequence.

Filtering changes the painted appearance after layout rather than altering the source image or the element's box dimensions. Because operations are sequential, changing their order can change the final result.

Full SVG filters form a graph of raster operations that can name intermediate results, merge branches, and combine source or backdrop inputs. That power has a runtime cost: a filtered object may require several offscreen layers, rasterizations, and pixel passes, especially when its source is animated. CSS filter-function shorthands simplify common effects and give the browser more opportunity to use an optimized path, but they do not replace the full primitive pipeline.

# References

[[css_thedefinitiveguide.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
