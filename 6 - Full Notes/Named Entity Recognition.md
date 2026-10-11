2026-09-05 16:28

Status: #baby

Tags: [[Natural Language Understanding Systems]]

# Named Entity Recognition

Named entity recognition finds spans of text that denote typed values such as people, places, organizations, dates, or quantities. In assistants, these values fill the arguments required by an [[Intent]].

Recognition can use grammars, gazetteers, or statistical sequence models. The output must often be normalized before the [[Dialog Manager]] can safely pass it to an external service.

In a text-mining pipeline, named-entity labels are a form of [[Semantic Text Enrichment]] applied before feature construction. Marking recognized entities as protected can keep later stemming or filtering from fragmenting a multiword name or changing its annotated form.

# References

[[aiassistants.epub]]

[[textminingandvisualization.pdf]]
