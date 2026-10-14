2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Waveguide Port Excitation

Waveguide port excitation applies a guided mode at a selected end face of a waveguide model. A numeric port uses a field pattern obtained from [[RF Boundary Mode Analysis]] rather than imposing a uniform scalar value across the opening.

For a two-port transmission calculation, the book assigns Port 1 to one end and Port 2 to the other, turns wave excitation on at Port 1, and leaves it off at Port 2. Port 2 still acts as the receiving and terminating reference for the [[Scattering Parameters|scattering-parameter]] solution.

The port assignment establishes the direction and reference planes of the experiment. Reversing the driven port or selecting the wrong boundary changes the question the model is answering.

# References

[[rfmodule.pdf]]
