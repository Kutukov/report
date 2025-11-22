import csv


def read_csv_files(filepaths: list[str]) -> list[dict]:
    rows = []
    for path in filepaths:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(reader)
    return rows
