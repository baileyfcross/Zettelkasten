from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


sys.stdout.reconfigure(encoding="utf-8", errors="replace")


ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "2 - Source Material" / "Books"
MANIFEST = Path(__file__).resolve().parent / "manifest.json"
FULL_NOTES = ROOT / "6 - Full Notes"
TAGS = ROOT / "3 - Tags"
TAG_REFERENCE_MINIMUM = 10
TAG_CHAPTER_MINIMUM_QUALIFYING_CHILDREN = 5
TAG_CHAPTER_MIN_WORDS = 500
TAG_CHAPTER_WORDS_PER_CHILD_TOPIC = 20


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inventory() -> None:
    previous = {}
    if MANIFEST.exists():
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        previous = {item["relative_path"].casefold(): item for item in data.get("sources", [])}

    files = sorted(
        (path for path in BOOKS.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(BOOKS).as_posix().casefold(),
    )
    sources = []
    for position, path in enumerate(files, start=1):
        relative_path = path.relative_to(BOOKS).as_posix()
        file_hash = sha256(path)
        old = previous.get(relative_path.casefold())
        unchanged = old is not None and old.get("sha256") == file_hash
        item = {
            "position": position,
            "relative_path": relative_path,
            "source_link": path.name,
            "extension": path.suffix.lower(),
            "size_bytes": path.stat().st_size,
            "sha256": file_hash,
            "status": old.get("status", "unprocessed") if unchanged else "unprocessed",
            "completed_at": old.get("completed_at") if unchanged else None,
            "concepts_created": old.get("concepts_created", []) if unchanged else [],
            "concepts_updated": old.get("concepts_updated", []) if unchanged else [],
            "notes_reused": old.get("notes_reused", 0) if unchanged else 0,
            "duplicate_candidates_merged": old.get("duplicate_candidates_merged", 0) if unchanged else 0,
            "parse_error": old.get("parse_error") if unchanged else None,
            "validation": old.get("validation") if unchanged else None,
        }
        sources.append(item)

    missing = [
        item["relative_path"]
        for key, item in previous.items()
        if item.get("status") == "processed"
        and key not in {source["relative_path"].casefold() for source in sources}
    ]
    manifest = {
        "schema_version": 1,
        "source_root": "2 - Source Material/Books",
        "order": "case-insensitive relative path",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_count": len(sources),
        "missing_previously_processed_sources": sorted(missing, key=str.casefold),
        "sources": sources,
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST} with {len(sources)} ordered sources")


def extract_pdf(relative_path: str, output: Path) -> None:
    source = BOOKS / Path(relative_path)
    reader = PdfReader(source)
    decryption = None
    if reader.is_encrypted:
        decryption = reader.decrypt("")
        if not decryption:
            raise RuntimeError("PDF requires a password and could not be decrypted")

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(f"SOURCE: {relative_path}\n")
        stream.write(f"PAGES: {len(reader.pages)}\n")
        stream.write(f"ENCRYPTED: {reader.is_encrypted}\n")
        stream.write(f"EMPTY_PASSWORD_DECRYPTION: {decryption}\n\n")
        extracted_pages = 0
        extracted_characters = 0
        for number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                extracted_pages += 1
            extracted_characters += len(text)
            stream.write(f"\n===== PDF PAGE {number} =====\n")
            stream.write(text)
            stream.write("\n")
    print(
        json.dumps(
            {
                "source": relative_path,
                "pages": len(reader.pages),
                "pages_with_text": extracted_pages,
                "characters": extracted_characters,
                "output": str(output),
            }
        )
    )


def page_numbers(specification: str, page_count: int) -> list[int]:
    numbers: set[int] = set()
    for part in specification.split(","):
        bounds = part.strip().split("-", maxsplit=1)
        start = int(bounds[0])
        end = int(bounds[1]) if len(bounds) == 2 else start
        if start < 1 or end > page_count or end < start:
            raise ValueError(f"Invalid page range: {part}")
        numbers.update(range(start, end + 1))
    return sorted(numbers)


def show_pdf_pages(relative_path: str, specification: str) -> None:
    source = BOOKS / Path(relative_path)
    reader = PdfReader(source)
    if reader.is_encrypted and not reader.decrypt(""):
        raise RuntimeError("PDF requires a password and could not be decrypted")
    for number in page_numbers(specification, len(reader.pages)):
        print(f"\n===== PDF PAGE {number} =====\n")
        print(reader.pages[number - 1].extract_text() or "")


def tracked_full_notes() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--", "6 - Full Notes"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {line.replace("\\", "/") for line in result.stdout.splitlines() if line}


def linked_topics(content: str) -> list[str]:
    match = re.search(r"^Tags:\s*(.*)$", content, re.MULTILINE)
    if not match:
        return []
    return [
        link.split("|", 1)[0].split("#", 1)[0].strip()
        for link in re.findall(r"\[\[([^\]]+)\]\]", match.group(1))
    ]


def parent_topics(content: str) -> list[str]:
    match = re.search(r"^Parent topics?:\s*(.*)$", content, re.MULTILINE)
    if not match:
        return []
    return [
        link.split("|", 1)[0].split("#", 1)[0].strip()
        for link in re.findall(r"\[\[([^\]]+)\]\]", match.group(1))
    ]


def wikilink_targets(content: str) -> set[str]:
    content_without_code = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    return {
        link.split("|", 1)[0].split("#", 1)[0].strip()
        for link in re.findall(r"\[\[([^\]]+)\]\]", content_without_code)
        if link.split("|", 1)[0].split("#", 1)[0].strip()
    }


def overview_chapter(content: str) -> str:
    heading = re.search(r"^## Overview Chapter\s*$", content, re.MULTILINE)
    if not heading:
        return ""
    remainder = content[heading.end() :]
    next_section = re.search(r"^##\s+", remainder, re.MULTILINE)
    return (remainder[: next_section.start()] if next_section else remainder).strip()


def directly_referenced_tags(content: str) -> str:
    heading = re.search(r"^## Directly Referenced Tags\s*$", content, re.MULTILINE)
    if not heading:
        return ""
    remainder = content[heading.end() :]
    next_section = re.search(r"^##\s+", remainder, re.MULTILINE)
    return (remainder[: next_section.start()] if next_section else remainder).strip()


def validate_topics() -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    counts: dict[str, int] = {}
    topic_notes: dict[str, list[str]] = {}
    tag_files = {path.stem.casefold(): path for path in TAGS.glob("*.md")}

    for path in sorted(FULL_NOTES.glob("*.md"), key=lambda item: item.name.casefold()):
        content = path.read_text(encoding="utf-8-sig")
        topics = linked_topics(content)
        if not topics:
            errors.append(f"{path.name}: missing linked topic on Tags line")
            continue
        for topic in topics:
            tag_path = tag_files.get(topic.casefold())
            if tag_path is None:
                errors.append(f"{path.name}: topic [[{topic}]] has no file in 3 - Tags")
                continue
            canonical_topic = tag_path.stem
            counts[canonical_topic] = counts.get(canonical_topic, 0) + 1
            topic_notes.setdefault(canonical_topic, []).append(path.stem)

    child_topics: dict[str, set[str]] = {path.stem: set() for path in tag_files.values()}
    for child_path in tag_files.values():
        content = child_path.read_text(encoding="utf-8-sig")
        for parent in parent_topics(content):
            parent_path = tag_files.get(parent.casefold())
            if parent_path is None:
                errors.append(f"{child_path.name}: parent topic [[{parent}]] has no file in 3 - Tags")
                continue
            child_topics[parent_path.stem].add(child_path.stem)

    tag_details: dict[str, dict] = {}
    tag_tiers: dict[str, list[str]] = {
        "chapter_summary": [],
        "regular": [],
        "under_threshold": [],
    }
    chapter_summaries: dict[str, dict] = {}
    for topic_key, path in sorted(tag_files.items(), key=lambda item: item[1].name.casefold()):
        topic = path.stem
        direct_references = counts.get(topic, 0)
        content = path.read_text(encoding="utf-8-sig")
        children = sorted(child_topics[topic], key=str.casefold)
        qualifying_children = [
            child for child in children if counts.get(child, 0) >= TAG_REFERENCE_MINIMUM
        ]
        chapter_required = (
            len(qualifying_children) >= TAG_CHAPTER_MINIMUM_QUALIFYING_CHILDREN
        )
        if chapter_required:
            tier = "chapter_summary"
        elif direct_references >= TAG_REFERENCE_MINIMUM:
            tier = "regular"
        else:
            tier = "under_threshold"
        tag_tiers[tier].append(topic)
        tag_details[topic] = {
            "tier": tier,
            "direct_references": direct_references,
            "child_tags": len(children),
            "qualifying_child_tags": len(qualifying_children),
        }

        chapter = overview_chapter(content)
        tag_section = directly_referenced_tags(content)
        expected_query = f'path:"6 - Full Notes" "[[{topic}]]"'
        if not chapter_required:
            if tier == "under_threshold":
                errors.append(
                    f"{path.name}: only {direct_references} directly linked Full Notes and "
                    f"{len(qualifying_children)} qualifying child tags; a tag requires at least "
                    f"{TAG_REFERENCE_MINIMUM} direct references or "
                    f"{TAG_CHAPTER_MINIMUM_QUALIFYING_CHILDREN} child tags with at least "
                    f"{TAG_REFERENCE_MINIMUM} references each"
                )
            if expected_query not in content:
                errors.append(
                    f"{path.name}: regular tags must query directly linked Full Notes for [[{topic}]]"
                )
            if tag_section:
                errors.append(
                    f"{path.name}: only chapter-summary tags may contain a "
                    "'## Directly Referenced Tags' section"
                )
            if chapter:
                errors.append(
                    f"{path.name}: has an Overview Chapter but only "
                    f"{len(qualifying_children)} child tags meet the "
                    f"{TAG_REFERENCE_MINIMUM}-reference threshold"
                )
            continue

        if direct_references:
            errors.append(
                f"{path.name}: chapter-summary tags cannot have directly linked Full Notes; "
                f"move its {direct_references} notes to focused child tags"
            )
        if expected_query in content:
            errors.append(
                f"{path.name}: replace the direct Full Notes query with a "
                "'## Directly Referenced Tags' section"
            )
        if not tag_section:
            errors.append(
                f"{path.name}: chapter-summary tags require a populated "
                "'## Directly Referenced Tags' section"
            )
        else:
            expected_tag_query = f'path:"3 - Tags" "[[{topic}]]"'
            if expected_tag_query not in tag_section:
                errors.append(
                    f"{path.name}: Directly Referenced Tags must query tag pages linking "
                    f"[[{topic}]] with '{expected_tag_query}'"
                )
            manual_tag_links = sorted(wikilink_targets(tag_section), key=str.casefold)
            if manual_tag_links:
                manual = ", ".join(f"[[{tag}]]" for tag in manual_tag_links)
                errors.append(
                    f"{path.name}: replace manually listed child tags with the embedded "
                    f"tag query; manual links found: {manual}"
                )

        minimum_words = max(
            TAG_CHAPTER_MIN_WORDS,
            len(children) * TAG_CHAPTER_WORDS_PER_CHILD_TOPIC,
        )
        word_count = len(re.findall(r"\b[\w'’-]+\b", chapter))
        chapter_links = {target.casefold() for target in wikilink_targets(chapter)}
        missing_children = [child for child in children if child.casefold() not in chapter_links]
        chapter_summaries[topic] = {
            "direct_references": direct_references,
            "child_topics": len(children),
            "qualifying_child_topics": len(qualifying_children),
            "chapter_words": word_count,
            "minimum_words": minimum_words,
        }

        if not chapter:
            errors.append(
                f"{path.name}: {len(qualifying_children)} child tags have at least "
                f"{TAG_REFERENCE_MINIMUM} references; add a textbook-style "
                "'## Overview Chapter' section covering all child topics"
            )
            continue
        if word_count < minimum_words:
            errors.append(
                f"{path.name}: overview chapter has {word_count} words; "
                f"write at least {minimum_words} words to synthesize its linked topics"
            )
        if missing_children:
            missing = ", ".join(f"[[{child}]]" for child in missing_children)
            errors.append(f"{path.name}: overview chapter does not cover child topics: {missing}")

    return {
        "full_notes": len(list(FULL_NOTES.glob("*.md"))),
        "used_topics": len(counts),
        "tag_reference_minimum": TAG_REFERENCE_MINIMUM,
        "chapter_summary_rule": {
            "minimum_qualifying_child_tags": TAG_CHAPTER_MINIMUM_QUALIFYING_CHILDREN,
            "minimum_direct_references_per_child": TAG_REFERENCE_MINIMUM,
        },
        "topic_counts": dict(sorted(counts.items(), key=lambda item: item[0].casefold())),
        "topic_notes": dict(sorted(topic_notes.items(), key=lambda item: item[0].casefold())),
        "tag_tiers": tag_tiers,
        "tag_details": tag_details,
        "chapter_summaries": chapter_summaries,
        "errors": errors,
        "warnings": warnings,
    }


def validate_source(relative_path: str) -> dict:
    source = BOOKS / Path(relative_path)
    source_link = f"[[{source.name}]]"
    note_paths = sorted(
        (
            path
            for path in FULL_NOTES.glob("*.md")
            if source_link in path.read_text(encoding="utf-8-sig")
        ),
        key=lambda path: path.name.casefold(),
    )
    all_files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]
    resolvable = {path.name.casefold() for path in all_files}
    resolvable.update(path.stem.casefold() for path in all_files)
    errors: list[str] = []
    warnings: list[str] = []
    wikilink_count = 0

    for path in note_paths:
        content = path.read_text(encoding="utf-8-sig")
        if not re.search(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", content, re.MULTILINE):
            errors.append(f"{path.name}: missing date/time")
        if not re.search(r"^Status:\s+#[A-Za-z0-9_-]+\s*$", content, re.MULTILINE):
            errors.append(f"{path.name}: missing Status")
        if not re.search(r"^Tags:\s+\[\[", content, re.MULTILINE):
            errors.append(f"{path.name}: missing linked Tags")
        title_match = re.search(r"^# ([^#\n].*)$", content, re.MULTILINE)
        if not title_match or title_match.group(1).strip() != path.stem:
            errors.append(f"{path.name}: title does not match filename")
        reference_match = re.search(r"^# References\s*$", content, re.MULTILINE)
        if not reference_match:
            errors.append(f"{path.name}: missing References section")
        elif source_link not in content[reference_match.end() :]:
            errors.append(f"{path.name}: source link is not under References")
        if "\x00" in content or "�" in content:
            errors.append(f"{path.name}: contains corrupt text characters")

        for topic in linked_topics(content):
            if not (TAGS / f"{topic}.md").is_file():
                errors.append(f"{path.name}: topic [[{topic}]] has no file in 3 - Tags")

        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        wikilink_count += len(links)
        for link in links:
            target = link.split("|", 1)[0].split("#", 1)[0].strip()
            if not target:
                errors.append(f"{path.name}: empty wikilink")
                continue
            target_name = Path(target.replace("\\", "/")).name.casefold()
            if target_name not in resolvable:
                errors.append(f"{path.name}: unresolved wikilink [[{link}]]")

    basename_groups: dict[str, list[str]] = {}
    for path in all_files:
        if path.suffix.lower() not in {".md", ".pdf", ".epub"}:
            continue
        basename_groups.setdefault(path.stem.casefold(), []).append(str(path.relative_to(ROOT)))
    duplicates = [paths for paths in basename_groups.values() if len(paths) > 1]
    if duplicates:
        warnings.extend("duplicate basename: " + "; ".join(paths) for paths in duplicates)

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entry = next(
        item for item in data["sources"] if item["relative_path"].casefold() == relative_path.casefold()
    )
    if sha256(source) != entry["sha256"]:
        errors.append(f"{relative_path}: source hash changed during processing")

    topic_validation = validate_topics()
    errors.extend(topic_validation["errors"])
    warnings.extend(topic_validation["warnings"])

    tracked = tracked_full_notes()
    created = []
    updated = []
    for path in note_paths:
        relative = path.relative_to(ROOT).as_posix()
        (updated if relative in tracked else created).append(path.stem)

    return {
        "source": relative_path,
        "contributing_notes": len(note_paths),
        "concepts_created": created,
        "concepts_updated": updated,
        "wikilinks_in_contributing_notes": wikilink_count,
        "topic_counts": topic_validation["topic_counts"],
        "errors": errors,
        "warnings": warnings,
    }


def complete_source(relative_path: str) -> None:
    validation = validate_source(relative_path)
    if validation["errors"]:
        raise RuntimeError(json.dumps(validation, indent=2))
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entry = next(
        item for item in data["sources"] if item["relative_path"].casefold() == relative_path.casefold()
    )
    entry["status"] = "processed"
    entry["completed_at"] = datetime.now(timezone.utc).isoformat()
    entry["concepts_created"] = validation["concepts_created"]
    entry["concepts_updated"] = validation["concepts_updated"]
    entry["notes_reused"] = len(validation["concepts_updated"])
    entry["duplicate_candidates_merged"] = 0
    entry["parse_error"] = None
    entry["validation"] = {
        "contributing_notes": validation["contributing_notes"],
        "wikilinks_in_contributing_notes": validation["wikilinks_in_contributing_notes"],
        "topic_counts": validation["topic_counts"],
        "errors": validation["errors"],
        "warnings": validation["warnings"],
    }
    MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


def refresh_processed_validations() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    refreshed = []
    for entry in data["sources"]:
        if entry.get("status") != "processed":
            continue
        validation = validate_source(entry["relative_path"])
        if validation["errors"]:
            raise RuntimeError(json.dumps(validation, indent=2))
        entry["validation"] = {
            "contributing_notes": validation["contributing_notes"],
            "wikilinks_in_contributing_notes": validation["wikilinks_in_contributing_notes"],
            "topic_counts": validation["topic_counts"],
            "errors": validation["errors"],
            "warnings": validation["warnings"],
        }
        refreshed.append(entry["relative_path"])
    MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"refreshed_processed_sources": refreshed}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("inventory")
    extract_parser = subparsers.add_parser("extract-pdf")
    extract_parser.add_argument("relative_path")
    extract_parser.add_argument("output", type=Path)
    show_parser = subparsers.add_parser("show-pdf-pages")
    show_parser.add_argument("relative_path")
    show_parser.add_argument("pages")
    validate_parser = subparsers.add_parser("validate-source")
    validate_parser.add_argument("relative_path")
    complete_parser = subparsers.add_parser("complete-source")
    complete_parser.add_argument("relative_path")
    subparsers.add_parser("validate-topics")
    subparsers.add_parser("refresh-processed-validations")
    args = parser.parse_args()

    if args.command == "inventory":
        inventory()
    elif args.command == "extract-pdf":
        extract_pdf(args.relative_path, args.output)
    elif args.command == "show-pdf-pages":
        show_pdf_pages(args.relative_path, args.pages)
    elif args.command == "validate-source":
        print(json.dumps(validate_source(args.relative_path), indent=2))
    elif args.command == "complete-source":
        complete_source(args.relative_path)
    elif args.command == "validate-topics":
        print(json.dumps(validate_topics(), indent=2))
    elif args.command == "refresh-processed-validations":
        refresh_processed_validations()


if __name__ == "__main__":
    main()
