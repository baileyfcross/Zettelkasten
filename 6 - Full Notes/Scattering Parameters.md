2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Scattering Parameters

Scattering parameters describe an RF or microwave component through the complex wave relationships at its ports. The method uses matched-load terminations rather than open- or short-circuit terminations at the main signal ports, making it suitable for multiport frequency-domain calculations.

In a two-port waveguide model, the ports define the input and output reference planes. The coefficient $S_{11}$ represents the Port 1 scattering response used by the book to calculate [[Voltage Standing Wave Ratio]]. A frequency sweep turns each parameter into a response curve rather than a single value.

Because both magnitude and phase matter, the parameter set is naturally handled with complex matrices. It provides a compact interface-level description even when the internal field distribution is spatially complicated.

# References

[[rfmodule.pdf]]
