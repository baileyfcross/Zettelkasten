2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX Selection and Focus Models

JavaFX separates a control's selected items from its internal focus. `SingleSelectionModel` allows one selected value, while `MultipleSelectionModel` exposes selected indices and items for controls that permit several rows. Controls such as tab panes use single selection, whereas list and table views can be configured for multiple selection.

Keyboard focus normally identifies which node receives input when a user tabs through an interface. The focus models in `ListView`, `TreeView`, `TableView`, and `TreeTableView` instead describe the internally focused row or value within that control. Keeping selection and focus distinct lets applications observe, move, or bind each state explicitly. A master-detail form can listen to selected-item changes while preserving a separate keyboard interaction path through [[JavaFX Event Handling]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
