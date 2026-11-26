import os
from pathlib import Path

ENTRY = "Diagnosis: you do not avoid decisions; you hold elections among imaginary versions of yourself, then demand a recount."


def output_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    output_path().write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
