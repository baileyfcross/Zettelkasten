2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Stroke Geometry

An SVG stroke is a derived painted region constructed around a path. `stroke-width` establishes its thickness, line joins determine how adjoining segments meet, and line caps determine how open ends are extended. Miter limits prevent acute joins from producing arbitrarily long spikes by switching to a safer join when the ratio becomes too large.

Dash arrays alternate painted and unpainted lengths along the path, while dash offset shifts the phase of that pattern. These lengths follow the current user coordinate system and can be combined with round caps to turn short dashes into dots. `vector-effect: non-scaling-stroke` can keep the apparent width stable when geometry is transformed, although other geometry still follows the transform.

Because the stroke is real geometry, it affects crispness, bounding regions, paint-server behavior, and the hit area used by [[SVG Pointer Event Hit Testing]]. [[SVG Line Markers]] are positioned from the underlying path vertices rather than from the outer edge of this stroked region.

# References

[[usingsvgwithcss3andhtml5.pdf]]

