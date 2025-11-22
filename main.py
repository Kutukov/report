from cli import parse_args
from reader.csv_reader import read_csv_files
from reports.registry import get_report, available_reports
from tabulate import tabulate


def main():
    args = parse_args(available_reports())
    rows = read_csv_files(args.files)

    report = get_report(args.report)
    result = report.calculate(rows)

    print(tabulate(result, headers=report.headers(), tablefmt="grid"))


if __name__ == "__main__":
    main()
