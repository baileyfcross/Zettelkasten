2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Feature-Map Inclusion

The paper proves that every feature map obtainable from its standard single-encoding quantum generator is also obtainable from the style-qGAN circuit. The containment follows because the trainable multipliers on later latent injections can be set to zero, reducing those gates to latent-independent variational operations and recovering the standard architecture.

This is an inclusion result about representable quantum feature maps, not a proof that adversarial training will find a better solution. The style-based circuit has additional degrees of freedom and can equal the standard model in the worst case, but optimization, sampling noise, and hardware errors still determine practical performance.

The constructive reduction suggests a transfer strategy: initialize the shared parameters from a trained standard qGAN and initially suppress the added latent-dependent terms. Training can then explore the larger style-qGAN parameter space without discarding the baseline solution.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

