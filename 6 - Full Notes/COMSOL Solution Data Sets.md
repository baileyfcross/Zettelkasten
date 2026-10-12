2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Thermal Results and Reporting]]

# COMSOL Solution Data Sets

COMSOL data sets identify the solution, parameter value, time, geometric representation, or transformed view on which a result operation acts. A study can produce several solution branches, and a sweep can add many parameter-indexed cases to the same model.

Choosing the wrong data set can produce a valid-looking plot of the wrong run. Result nodes should therefore record their source explicitly, especially when a two-dimensional axisymmetric solution is revolved for three-dimensional display or when [[COMSOL Cut Points Lines and Planes|cuts]] are derived from a volume.

# References

[[cosmolheattransfermodels.pdf]]

