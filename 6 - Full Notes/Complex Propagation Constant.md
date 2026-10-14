2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Complex Propagation Constant

A complex propagation constant combines attenuation and phase progression for a sinusoidal electromagnetic wave traveling through a material. Writing the spatial factor as

$$
e^{-kz}=e^{-\alpha z}e^{-j\beta z}
$$

separates the amplitude decay rate $\alpha$ from the phase rate $\beta$.

The attenuation term depends on angular frequency and material properties including permittivity, permeability, and conductivity. Its reciprocal defines [[Electromagnetic Skin Depth]], while the phase term determines how the oscillation advances with distance.

Keeping both parts is essential in microwave modeling because a field can lose magnitude and shift phase at the same time. Treating the propagation factor as purely real would discard the phase relationship used by impedance and scattering calculations.

# References

[[rfmodule.pdf]]
