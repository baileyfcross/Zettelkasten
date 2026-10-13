2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Keyboard Focus Management

Keyboard interaction requires both a focusable element and behavior that matches its role. SVG links provide the native baseline: they enter the tab order and activate with Enter in most of the book's target browsers. A script that makes a link behave like a button must also support Space, prevent the page-scroll default, and expose `role="button"` so behavior and semantics agree.

SVG 2 adopts the HTML `tabindex` and `focus()` model. `tabindex="0"` adds an element to normal sequential focus, while `-1` permits scripted focus without adding another tab stop. Positive values create a priority order and are generally avoided. Complex widgets can move focus with arrow keys, but the source documents incomplete implementation in its 2017 browser landscape.

Native HTML controls should be preferred when they can perform the task. An HTML input may be visually hidden while still handling keyboard and screen-reader behavior, with its state reflected into SVG. Whatever the implementation, visible focus styling, [[SVG ARIA Roles and Label Relationships|accurate roles and names]], and parity with pointer input are part of one control contract. See [[SVG Graphical Hyperlinks]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

