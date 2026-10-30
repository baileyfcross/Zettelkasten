2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java UTF-8 Default Charset

Modern Java uses UTF-8 as the default charset so text operations that omit an explicit encoding behave consistently across operating systems and regional settings. This reduces platform-dependent corruption when producers and consumers handle non-ASCII characters.

The portability improvement can change legacy behavior that implicitly depended on the host's native encoding. Such code should state the intended charset explicitly or deliberately consult the native-encoding property rather than assuming the previous environment-specific default.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
