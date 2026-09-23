# Book-to-Zettelkasten handoff for another Codex

Use this guide when the user asks to continue onto the next book in this vault. Work in the repository root. Process **exactly one source per request**, then stop. The next source is the first `unprocessed` entry in `.zettelkasten-processing/manifest.json` in its stored, case-insensitive relative-path order. Read the current manifest; do not rely on a book name remembered from an earlier session.

Do not stage, commit, or push. The user reserves all Git publication steps for themselves. Do not edit `.obsidian/`, move or modify source books, delete existing notes, or overwrite unrelated local changes.

## Authority and starting checks

- `2 - Source Material/Books/` is the **only factual source** for new book-derived knowledge. Do not use the web, external summaries, or background knowledge to fill gaps. Other vault notes are useful for terminology, deduplication, style, links, and material already written; do not mistake an unsupported existing statement for evidence from the current book.
- Read `5 - Templates/Full Note.md`, inspect several recent Full Notes and tag pages, and inspect `.zettelkasten-processing/prepare_sources.py`. If repository or tool instructions require a format-specific skill (such as PDF), follow it.
- Run `git status --short` before editing. Preserve all user changes. In particular, a prior book may be finished in the manifest but still uncommitted; do not redo or overwrite it merely because its files are untracked.
- Check the manifest entry's `relative_path`, `status`, and `sha256` against the actual source. If a processed book's hash changed, flag it for reinspection instead of silently treating it as unchanged. If a source is missing or unreadable, record the problem and do not invent notes or mark it processed.
- The helper script can refresh the inventory, extract PDF text, validate notes/topics, and complete a source. Inspect its behavior before running mutating commands. `inventory` rewrites the manifest and should be used when the source library changes, not reflexively on every continuation.

## Read and map one book

1. Extract the **whole** source locally. For PDFs, a possible command is `python .zettelkasten-processing/prepare_sources.py extract-pdf "relative/path.pdf" "tmp/pdfs/book.txt"`; `pdfplumber` or another local extractor may be more practical for a difficult or slow PDF. For EPUBs, inspect the spine/navigation and extract readable chapter text. Keep temporary extraction under `tmp/` and remove only your own verified scratch files when finished. Never alter the source book.
2. Inspect the contents, introduction, substantive chapters, examples, definitions, conclusion, glossary/index, and meaningful diagrams or tables. Check representative pages visually when text extraction may lose a diagram, equation, column order, or caption. Record extraction gaps; do not infer missing content from a table of contents.
3. Build a provisional inventory of reusable concepts, relationships, prerequisites, techniques, and domain-specific distinctions. A heading is a lead, not an automatic note. Favor notes that explain an independently useful idea; do not create an overall book summary or one note per chapter.
4. For every candidate, search `6 - Full Notes/`, `3 - Tags/`, and the rest of the vault for exact names, case variants, singular/plural forms, acronyms, and synonyms. Reuse an existing canonical Full Note whenever it represents the same concept. Keep different domain meanings separate when the book supports the distinction. Preserve existing content and references when updating; synthesize the new contribution into the concept rather than appending disconnected book-by-book summaries.
5. Give each note a concise definition, explanation of mechanism or significance, and a small example or qualification where it helps. Link meaningful prerequisites and related concepts with Obsidian `[[wikilinks]]`. Verify every new conceptual link resolves; create a prerequisite note only if the source actually supports it. Do not create dictionary entries for ordinary words, copy long book passages, or silently modernize version-specific claims.

## Full Note format

Create new knowledge files only in `6 - Full Notes/`, with a canonical title matching the filename. Use the real local date and time, not template placeholders:

```markdown
2026-09-22 10:30

Status: #baby

Tags: [[Focused Topic]]

# Canonical Concept Name

An original-language explanation grounded in the book, with meaningful [[Related Concept]] links.

# References

[[exact-source-filename.pdf]]
```

The date above is an example; use the actual timestamp. `Tags:` should normally name one focused tag, adding a second only for a genuine cross-domain concept. A reused note can retain relevant existing tags. The source reference must use the exact local filename, appear under `# References`, and be added only when this source materially contributed knowledge. Preserve all older references. If duplicate source basenames exist in different folders, use an unambiguous Obsidian path-qualified link.

## Topic and chapter hierarchy

The live rules are encoded in `.zettelkasten-processing/prepare_sources.py` (`validate_topics`); read that function before reorganizing tags. Current convention:

- A regular topic tag has **at least 10 directly linked Full Notes**. Aim for roughly **10–20**; when it grows beyond 20, split it into meaningful narrower topics rather than creating arbitrary tiny tags. Do not create a regular tag with only one or two notes to hold the current book's leftovers. Group those concepts with a valid focused topic or retain a provisional concept relationship until a defensible topic exists.
- Every regular tag has a file in `3 - Tags/`, a concise description, and a dynamic query for its direct Full Notes. If it belongs under a parent, include `Parent topic: [[Parent Tag]]` (or `Parent topics:` for genuine multiple parents). Do not manually maintain a backlink list.
- A parent becomes a **chapter-summary tag** when it has at least **five child tags**, each with **at least 10 directly linked Full Notes**. It has **zero directly linked Full Notes** of its own. Only this tier gets an `## Overview Chapter` synthesizing all child topics in original prose, at least `max(500, 20 × number of child tags)` words, plus the dynamic child-tag query. The chapter must link each child topic meaningfully. A parent with four qualifying children, or five children of which only four meet the threshold, does not qualify.
- Do not put an `## Overview Chapter` or `## Directly Referenced Tags` section on ordinary child tags. When a parent crosses the chapter threshold, move any direct Full Notes to appropriate focused children before validating. Keep the parent-child links intact.

Regular tag example:

````markdown
# Focused Topic

Parent topic: [[Parent Tag]]

Brief description of the topic.

## Directly Linked Full Notes

```query
path:"6 - Full Notes" "[[Focused Topic]]"
```
````

Chapter tag's backlink section (after its chapter prose):

````markdown
## Directly Referenced Tags

```query
path:"3 - Tags" "[[Chapter Tag]]"
```
````

The `query` blocks are Obsidian searches. They let the vault display linked notes/tags dynamically; do not replace them with a manually edited list. Existing examples include `3 - Tags/Software Design Principles.md` and `3 - Tags/Software Design Patterns and Application Architecture.md`.

## Validate and record completion

Before changing the manifest to `processed`:

1. Check that every created or updated note has a valid timestamp, `Status:`, `Tags:`, a filename-matching `#` title, `# References`, and the exact source link under References. Check that the explanation truly came from this book, is atomic, and leaves older material intact.
2. Check every new wikilink, tag file, parent-child link, direct note count, and chapter threshold. A top-tier tag must have zero direct Full Notes and the child-tag query; child tags must have the direct-Full-Note query. Search for duplicate or near-duplicate concept names before declaring the book done.
3. Run `python .zettelkasten-processing/prepare_sources.py validate-source "relative/path.pdf"` and inspect **all** errors and warnings. Run `python .zettelkasten-processing/prepare_sources.py validate-topics` when changing the taxonomy. Fix introduced errors rather than relaxing the validator. The helpers validate the whole vault as well as the current source, so distinguish pre-existing issues from new ones.
4. Check `git diff --check`, `git status --short`, and source-file hashes or diffs. Verify only intended notes, tag pages, and the manifest changed; check untracked new notes separately because `git diff --check` omits them.
5. Only after the source is fully processed and validation succeeds, update its manifest entry: `status: processed`, completion time, created/updated concepts, reuse/deduplication counts, and validation results. `python .zettelkasten-processing/prepare_sources.py complete-source "relative/path.pdf"` can do this, but it classifies created versus updated using Git tracking: **if earlier uncommitted notes are present, verify and correct those counts rather than trusting them blindly**. Do not mark a partially read or unparseable book processed. Keep `parse_error` descriptive when parsing fails.
6. Re-read the manifest to confirm the just-finished source is processed and the next source is still unprocessed. Remove only your own temporary extraction after checking its resolved path is inside the workspace. Do not process the next book in the same request.

Report the book processed, new and updated Full Notes, tag/chapter changes, validation outcome, and the exact next source. Explicitly state that nothing was staged, committed, or pushed. If blocked, report the verified stopping point without claiming the source complete.

## Copy-paste prompt for a fresh Codex task

> Work in this Zettelkasten repository. Read `.zettelkasten-processing/BOOK_PROCESSING_INSTRUCTIONS.md`, `5 - Templates/Full Note.md`, the processing manifest, and the helper script. Process exactly the next unprocessed source in manifest order into atomic, cross-linked Full Notes, reusing canonical notes and following the 10-reference topic / five-qualified-child chapter rules. Use only the local source book for new factual content. Validate the result, update the manifest only when complete, and stop after that one book. Preserve existing work. Do not stage, commit, or push.
