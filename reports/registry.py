from .performance import PerformanceReport

REPORTS = {
    "performance": PerformanceReport(),
}


def get_report(name: str):
    report = REPORTS.get(name)
    return report


def available_reports():
    return REPORTS.keys()
