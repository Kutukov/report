import argparse
import os
from pathlib import Path


def parse_args(available_reports: tuple) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Генератор отчётов")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Один или несколько CSV файлов"
    )
    parser.add_argument(
        "--report",
        required=True,
        help=f"типы отчётов ({', '.join(available_reports)})",
    )
    args = parser.parse_args()

    validate_args(args, available_reports)

    return args


def validate_args(args: argparse.Namespace, available_reports: tuple) -> None:

    files = []
    for p in args.files:
        path = Path(p)
        if not path.exists():
            raise ValueError(f"File not found: {p}")
        if not os.access(path, os.R_OK):
            raise ValueError(f"not readable: {p}")
        files.append(str(path.resolve()))

    # удаление дубликатов
    seen = set()
    deduped = []
    for f in files:
        if f not in seen:
            deduped.append(f)
            seen.add(f)
    args.files = deduped

    if args.report not in available_reports:
        raise ValueError(
            f"Unknown report: {args.report}. Available: {', '.join(available_reports)}"
        )
