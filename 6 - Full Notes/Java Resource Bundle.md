2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java Resource Bundle

A Java resource bundle maps stable keys to locale-specific values. Bundles can be supplied through property files or classes whose base name is combined with language and region suffixes to select the best available match.

Code asks for a key rather than embedding translated text, separating program logic from language content. The lookup process falls back from a specific locale toward more general bundles, so a base bundle should contain complete defaults. Translators can change values without changing the keys expected by code.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
