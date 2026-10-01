2026-10-01 00:39

Status: #baby

Tags: [[3D Game Rendering]]

# Radiosity Rendering

Radiosity treats illumination as an exchange of energy among diffuse surfaces. A scene is divided into patches, and the method solves for the equilibrium amount of light leaving each patch after accounting for emitted energy and energy arriving from other patches.

Because the lighting solution belongs to the surfaces rather than to a particular eye position, it can be reused for multiple views of a static environment. The method captures indirect diffuse illumination and color transfer, complementing the path-by-path visibility of [[Ray Trace Rendering]]. Its cost lies in computing the geometric coupling among many surface elements.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
