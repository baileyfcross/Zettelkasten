2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX Table and Tree Controls

`ListView` presents a flat sequence, while `TreeView` uses `TreeItem` objects to represent an expandable hierarchy. `TableView` divides row objects across `TableColumn` instances whose value factories select data and whose cell factories control display or editing. `TreeTableView` combines the hierarchy of `TreeView` with column-based presentation through `TreeTableColumn`.

These controls normally read from observable data so additions, removals, and permutations can update the view. A sorted wrapper can keep visible items ordered, and an extractor can report changes inside mutable list elements when those properties affect sorting. Because rendering is virtualized, display customization belongs in [[JavaFX Virtualized Cells and Factories]], while row navigation belongs in [[JavaFX Selection and Focus Models]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
