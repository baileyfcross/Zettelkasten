2026-09-15 02:20

Status: #baby

Tags: [[Neural Network Training]]

# Layer-Wise Autoencoder Pretraining

Greedy layer-wise pretraining trains one [[Autoencoder|encoder]] on raw inputs, keeps its encoding layer, and then trains another encoder to reconstruct that first layer's representation. Repeating this builds a stack of representations before the final prediction task is fitted.

Each layer is optimized for its own reconstruction task rather than the eventual output, which is why the process is called greedy. A later tuning phase can freeze the pretrained layers or adjust the whole network using target labels. Kelleher presents this as an important historical route to useful initial weights for deep networks, while noting that most later deep networks are trained without it.

# References

[[deeplearning_mit.epub]]
