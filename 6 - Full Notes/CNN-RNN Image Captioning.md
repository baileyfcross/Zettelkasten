2026-09-15 02:16

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# CNN-RNN Image Captioning

An image-captioning model can combine a [[Convolutional Neural Network]] encoder with a recurrent language decoder. The CNN analyzes the image and produces a vector representation; the recurrent component uses that vector as context while generating a description word by word.

Kelleher presents this as an intermodal variant of an [[Encoder-Decoder Network]]: the input is visual, but the output is a language sequence. The useful abstraction is not that a fixed vector perfectly captures an image's meaning; it is that learned representations can connect two different data forms in one trainable architecture.

# References

[[deeplearning_mit.epub]]
