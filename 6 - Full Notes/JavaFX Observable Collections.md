2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# JavaFX Observable Collections

JavaFX supplies `ObservableList`, `ObservableMap`, `ObservableSet`, and observable arrays so changes to a collection can update controls and bindings. `FXCollections` creates the framework implementations and provides list operations such as sort, shuffle, rotate, copy, and replace while minimizing the number of notifications produced.

Collection listeners expose change-specific information. A list change cursor can report additions, removals, replacements, and permutations; map and set changes identify affected entries; observable arrays track a changed range while retaining separate size and capacity behavior. Content bindings can synchronize ordinary and observable collections or two observable collections. These structures are the data source for list and table controls described in [[JavaFX Virtualized Cells and Factories]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
