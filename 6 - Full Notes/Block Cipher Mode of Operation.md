2026-10-18 16:30

Status: #baby

Tags: [[Symmetric Encryption Algorithms and Modes]]

# Block Cipher Mode of Operation

A block cipher mode of operation defines how a fixed-size cipher is applied across a message containing multiple blocks. Electronic Codebook processes each block independently. Cipher Block Chaining combines each plaintext block with the preceding ciphertext and begins from an [[Initialization Vector]]. Cipher Feedback and Output Feedback reuse cipher output as feedback, while Counter mode combines plaintext with encrypted, successively incremented counter values.

The mode changes what structure is carried from one block to the next and what setup data must be unique or unpredictable. Selecting an algorithm such as the [[Advanced Encryption Standard]] therefore does not finish the design; the mode and its surrounding parameters are part of the security behavior.

# References

[[cryptographyandcryptanalysisinjava.epub]]
