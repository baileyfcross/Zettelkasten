2026-09-27 18:30

Status: #baby

Tags: [[AI-Assisted Network Automation]]

# Text-to-Topology Generation

Text-to-topology generation asks a language model to translate a written network description into a formal graph representation. Devices become nodes, links become edges, and labels can preserve interface, role, or subnet information that would otherwise remain buried in prose.

The translation is valuable because formal output can be rendered and inspected, but the model may omit a connection or invent one. The prompt should specify the expected graph language and required attributes. The resulting graph is then checked against the source description before [[Graphviz Network Topology Rendering]] turns it into a diagram.

# References

[[ainetworkingcookbook.pdf]]
