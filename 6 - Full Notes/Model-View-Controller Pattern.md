2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Application Architecture]] [[Object-Oriented Design Patterns]]

# Model-View-Controller Pattern

Model-View-Controller separates domain state in a model, visible representation in a view, and input coordination in a controller. In a mobile application, the controller receives user actions, selects model operations, and determines which view should be displayed next.

The separation keeps domain behavior out of platform UI classes, but the controller can become overly broad if navigation, service access, and presentation formatting are all concentrated in it. Clear controller scope is therefore part of applying the pattern.

In a web application, the same separation lets the view concentrate on presentation, the model represent application data, and the controller coordinate request logic. The value is the boundary among these responsibilities, not a guarantee that placing code in three folders automatically creates low coupling.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
