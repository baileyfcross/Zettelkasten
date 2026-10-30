2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Text Block

A Java text block is a multiline String literal delimited by three double quotes. It preserves a readable block layout while applying indentation rules that remove incidental leading space shared by the source lines.

Text blocks reduce concatenation and explicit newline escapes for embedded JSON, HTML, SQL, or formatted messages. They still produce ordinary immutable String objects and support escapes for cases where the natural block layout is not the desired runtime content. Their purpose is clearer source representation, not a new runtime text type.

The closing delimiter's position participates in incidental-indentation removal, and the opening delimiter must be followed by a line terminator. A trailing backslash can suppress an otherwise included line break, while `\s` can preserve a significant space that normal indentation processing might obscure.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
