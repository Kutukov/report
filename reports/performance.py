from .Base_report import BaseReport
from collections import defaultdict
from statistics import mean


class PerformanceReport(BaseReport):
    def headers(self):
        return ["position", "avg_performance"]

    def calculate(self, rows):
        performance_map = defaultdict(list)

        for row in rows:
            try:
                perf = float(row["performance"])
                position = row["position"]
                performance_map[position].append(perf)
            except (ValueError, KeyError):
                continue

        result = []
        for position, vals in performance_map.items():
            avg_perf = round(mean(vals), 2)
            item = (position, avg_perf)
            result.append(item)

        return sorted(result, key=lambda x: x[1], reverse=True)
