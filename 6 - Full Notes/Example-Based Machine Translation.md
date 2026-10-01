2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Example-Based Machine Translation

Example-based machine translation translates by analogy with fragments found in previously translated texts. It retrieves source passages similar to the new input, identifies their target-language counterparts, adapts them, and recombines them into a candidate sentence.

The method exploits contextual examples that a bilingual dictionary cannot provide and works especially well in repetitive technical sublanguages. Its weaknesses are coverage and recombination: exact matches are rare, retrieved fragments may overlap, and partial pieces may not form a grammatical whole. It consequently works well as a precise module inside a broader [[Hybrid Machine Translation]] system rather than as a complete solution by itself.

# References

[[machinetranslation.epub]]
