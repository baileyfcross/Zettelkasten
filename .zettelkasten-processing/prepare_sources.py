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
        "errors": validation["errors"],
        "warnings": validation["warnings"],
    }
    MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))


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


if __name__ == "__main__":
    main()
