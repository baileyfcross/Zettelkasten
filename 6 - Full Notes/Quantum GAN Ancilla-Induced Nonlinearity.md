2026-10-16 21:58

Status: #baby

Tags: [[Experimental Quantum GAN Image Generation]]

# Quantum GAN Ancilla-Induced Nonlinearity

A unitary quantum circuit transforms state amplitudes linearly, while a generative model must learn a nonlinear map from a latent distribution to a data distribution. The patch and batch qGANs introduce nonlinearity by partitioning the circuit into feature and ancillary subsystems, projecting the ancillas onto a selected outcome, and renormalizing the conditional feature state.

The normalization denominator depends on the input state and trainable circuit parameters. Dividing the projected state by this success probability makes the conditioned output a nonlinear function of the latent input. Computational-basis probabilities of the feature subsystem then provide the generator's classical pixel values.

This mechanism is a form of postselection. Its practical cost depends on how often the selected ancillary outcome occurs, but the experiment does not report a scaling analysis of that success probability. A classical activation could instead be applied after measurement, so ancilla conditioning is one available nonlinearity rather than a uniquely required construction.

# References

[[2021 - Experimental Quantum Generative Adversarial Networks for Image Generation.pdf]]
