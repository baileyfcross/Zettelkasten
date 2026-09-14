2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]]

# COMSOL Material Assignment

A material node supplies density, conductivity, heat capacity, viscosity, optical properties, and other coefficients required by active physics. Each domain must receive the properties needed by the equations solved there.

Built-in libraries offer convenient defaults, but the applicable temperature and pressure ranges must be checked. Measured tables or functions may be preferable for [[Temperature-Dependent Thermophysical Properties|variable properties]], and a [[Material Sweep in COMSOL|material sweep]] can compare alternatives without rebuilding the model.

# References

[[cosmolheattransfermodels.pdf]]

