2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Standard-Architecture Comparison

The paper compares the style-qGAN with a standard qGAN while holding constant three qubits, five latent dimensions, two layers, $3\times10^4$ epochs, a $10^4$-event training set, batch size 128, and two controlled-$R_Y$ entanglers. The difference is that the standard circuit encodes latent variables only once, while the style circuit uses [[Style-qGAN Latent Reuploading]].

The style model achieves KL divergences of $0.064$, $0.074$, and $0.050$ for $s$, $t$, and $y$, compared with $0.338$, $11.171$, and $0.049$ for the standard model. Repeated encoding therefore gives the largest improvement on the strongly non-Gaussian $s$ and $t$ distributions, while the Gaussian-like rapidity result is essentially unchanged.

The comparison is not parameter matched: [[Affine Latent Gate Encoding]] gives the style circuit 62 trainable parameters versus 36 in the standard circuit. Equalizing counts would require adding layers or otherwise changing the baseline architecture, so the experiment demonstrates an architectural result under matched depth rather than isolating reuploading from capacity.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

