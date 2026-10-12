# CSS Styling and Layout

Parent topic: [[Full-Stack Web Application Development]]

CSS Styling and Layout is the chapter-level topic for selecting document content, resolving competing declarations, formatting boxes and text, constructing layouts, and adapting visual presentation to media and interaction. Full Notes should link to one of the focused child topics rather than directly to this chapter tag.

## Overview Chapter

[[CSS Stylesheet Integration]] begins at the boundary between a document and its presentation. CSS may arrive through an external link, an embedded style element, an import rule, or an inline declaration. Each route changes where the rules live and how widely they can be reused, while the rule structure still joins selectors to declarations. Replaced elements, display roles, vendor prefixes, whitespace, and comments define the practical vocabulary in which those rules operate.

Once styles are available, [[CSS Selectors and Pseudo-Elements]] determines which document nodes they address. Element, class, ID, and attribute selectors identify content by different kinds of evidence. Combinators describe ancestry or sibling relationships, structural pseudo-classes use position within the document tree, and dynamic pseudo-classes respond to states such as hovering or focus. Pseudo-elements target generated or typographic portions that are not ordinary elements in the source document.

Matching alone does not decide the result. [[CSS Cascade and Inheritance]] resolves all declarations that can affect a property by comparing importance, origin, specificity, and source order. Inheritance can supply a value from an ancestor when the property permits it, and computed values translate the winning declaration into the form used for later layout. This ordered conflict-resolution process is the central mechanism behind the word “cascading.”

The declarations themselves draw on [[CSS Values Units and Colors]]. Keywords, strings, URLs, numbers, percentages, dimensions, resolutions, colors, and attribute-derived values have different syntactic and computational behavior. Absolute and relative units anchor measurements to different references, while `calc()` combines compatible quantities. RGB and HSL offer different descriptions of color, and custom properties provide scoped value substitution through identifiers beginning with two hyphens.

[[CSS Web Typography]] chooses and configures the fonts used to draw text. Generic families provide fallbacks, while `@font-face` describes downloadable resources and their usable ranges. Weight, size, style, stretch, kerning, variants, feature settings, synthesis, and the font shorthand all participate in font matching. The browser works through the declared family list and available faces until it finds a resource that can represent the requested text.

After a font is selected, [[CSS Text Layout and Decoration]] controls how glyphs occupy lines. Indentation and horizontal alignment shape blocks of text; line height and vertical alignment position inline boxes relative to a shared line box. Word spacing, letter spacing, transformations, decorations, and shadows alter appearance without changing the underlying document text. Whitespace, wrapping, hyphenation, writing mode, orientation, and direction determine where lines break and in which direction they progress.

Every displayed element participates in [[CSS Box Model and Normal Flow]]. Content, padding, borders, and margins form nested regions whose dimensions affect surrounding boxes. Containing blocks supply reference rectangles for percentages and positioning. Block, inline, inline-block, list-item, and replaced-element formatting create different box behaviors, while width, height, margin collapsing, overflow, and visibility decide how much space a box uses and what happens when content exceeds it.

[[CSS Borders Backgrounds and Shadows]] adds visible treatment around and behind those boxes. Padding separates content from a border; margins separate one box from others; and outlines provide emphasis without consuming layout space. Borders can vary by side, use rounded corners, or draw from an image. Background layers can be positioned, sized, clipped, repeated, and combined, while linear or radial gradients generate images and box shadows simulate offset or inset depth.

Before modern layout modules, authors often relied on [[CSS Floats Positioning and Shapes]]. Floats remove a box from ordinary block flow while allowing inline content to wrap around it, and clearing prevents later boxes from wrapping beside selected floats. Shapes refine the wrap boundary beyond a rectangle. Absolute, relative, fixed, and sticky positioning instead use offsets and containing blocks, with stacking levels deciding which overlapping boxes appear in front.

[[CSS Flexible Box Layout]] creates a one-dimensional formatting context whose items are arranged along a main axis and aligned along a cross axis. Direction and wrapping establish the available flex lines. Distribution and alignment properties allocate leftover space, while the flex basis, growth factor, and shrink factor determine how item sizes respond to the container. The visual order can differ from source order, but document and accessibility order still follow the source.

[[CSS Grid Layout]] provides a two-dimensional system of rows, columns, lines, cells, and named areas. Track sizing may use fixed lengths, content-aware functions, or fractional units, and repeated patterns can generate many tracks compactly. Explicit placement and auto-placement share the same grid, while the implicit grid grows when items fall outside the declared structure. Gaps, alignment, overlap, and stacking finish the layout without requiring content order to dictate visual position.

Structured content receives additional models in [[CSS Tables Lists and Generated Content]]. Table boxes are assembled from rows, columns, groups, cells, and captions, including anonymous boxes required to repair incomplete structures. Border models, layered backgrounds, sizing, and alignment control the rendered table. Lists use markers, images, and marker positions, while generated content and counters insert presentational text or numbering without changing the source markup.

Time and geometry meet in [[CSS Transforms Transitions and Animation]]. Two- and three-dimensional transform functions alter an element’s rendered coordinate space around a chosen origin and perspective. Transitions interpolate a changed property between states, with duration, delay, and timing functions controlling the route. Keyframe animations explicitly define intermediate states, repetitions, direction, fill, and play state. Motion remains an enhancement and should be constrained when it could trigger vestibular or seizure-related harm.

[[CSS Filters Blending Clipping and Masking]] changes how already-laid-out content is painted and combined. Filter functions can blur, shadow, brighten, recolor, or alter contrast. Blend modes calculate interactions between element or background colors, while isolation creates a controlled compositing group. Clipping uses a hard geometric boundary, whereas masking uses image values to vary visibility. Object fitting and positioning determine how replaced content occupies its content box.

Finally, [[CSS Media Queries and Print Styling]] makes presentation conditional on output conditions. Media types and feature descriptors test characteristics such as dimensions, orientation, or resolution, and logical operators combine those tests. Feature queries separately test property-value support for progressive enhancement. Paged-media rules introduce page boxes, margins, breaks, and print-specific styles so the same document can remain intelligible on screens and on physical pages.

Together, these topics describe CSS as a staged rendering language. Rules enter the document, selectors match elements, the cascade resolves values, formatting models construct boxes and lines, layout systems arrange them, and painting features determine their final appearance. Conditional rules then adapt that result to the capabilities and medium through which the document is presented.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[CSS Styling and Layout]]"
```
