2026-09-05 16:28

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Encoder-Decoder Network

An encoder-decoder network transforms an input sequence into an internal representation and then generates an output sequence. The encoder reads the source, while the decoder produces the target one step at a time.

The architecture supports mappings whose input and output lengths differ, including speech transcription and language generation. An [[Attention Mechanism]] can let the decoder consult different parts of the encoded input at each step.

Kelleher's sequence-to-sequence translation example uses one LSTM to read source words into a sentence vector and a second LSTM to generate target words. Each generated word is fed back as the next decoder input until an end marker appears. The representation connects two sequences, though a single fixed vector need not capture every nuance of a sentence. The same cross-domain pattern appears in [[CNN-RNN Image Captioning]], where an image encoder supplies the context for a language decoder.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
