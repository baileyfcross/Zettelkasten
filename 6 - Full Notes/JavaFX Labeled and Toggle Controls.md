2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX Labeled and Toggle Controls

JavaFX `Label`, `Button`, `CheckBox`, `Hyperlink`, `ToggleButton`, and `RadioButton` share the `Labeled` base, so they can combine text with a graphic and common alignment or font properties. A label's `labelFor` relationship associates descriptive text with another control, improving keyboard navigation and screen-reader output.

Toggle controls express persistent selection rather than a momentary action. A check box can optionally add an indeterminate state. Toggle buttons in a `ToggleGroup` permit at most one selected member and can allow none, while radio buttons in a group are styled and operated so a user selects a replacement rather than clearing the whole group. Their state can be observed through [[JavaFX Properties]] and styled through [[JavaFX CSS Selectors and Application]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
