2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Voltage Standing Wave Ratio

Voltage standing wave ratio, or VSWR, is a matching measure derived from the magnitude of the input reflection coefficient. For Port 1 in the book's model,

$$
\mathrm{VSWR}=\frac{1+|S_{11}|}{1-|S_{11}|}.
$$

A value near 1 indicates that very little of the incident wave is reflected at the input. Larger values indicate a stronger reflected component and therefore a less effective transfer of power between the source, component, and load.

Plotting VSWR over frequency reveals the usable transmission band. In the [[Three-Stub Tuner]] model, changing one stub height shifts the low-VSWR region, making the measure useful for both matching assessment and geometric tuning.

# References

[[rfmodule.pdf]]
