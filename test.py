import pytest
from types import SimpleNamespace
from cli import validate_args
from reports.registry import available_reports
from reports.performance import PerformanceReport
from pathlib import Path
import os


def test_validate_args_nonexistent_file(tmp_path):
    args = SimpleNamespace(files=["/no/such/file.csv"], report="performance")
    with pytest.raises(ValueError) as exc:
        validate_args(args, available_reports())
    assert "File not found" in str(exc.value)


def test_validate_args_unreadable_file(tmp_path, monkeypatch):
    f = tmp_path / "a.csv"
    f.write_text("name,position,performance\n")
    # Симулируем отсутствие чтения
    monkeypatch.setattr(os, "access", lambda p, m: False)
    args = SimpleNamespace(files=[str(f)], report="performance")
    with pytest.raises(ValueError) as exc:
        validate_args(args, available_reports())
    assert "not readable" in str(exc.value).lower()


def test_validate_args_unknown_report(tmp_path):
    f = tmp_path / "a.csv"
    f.write_text("name,position,performance\n")
    args = SimpleNamespace(files=[str(f)], report="unknown_report")
    with pytest.raises(ValueError) as exc:
        validate_args(args, available_reports())
    assert "Unknown report" in str(exc.value)


def to_dict_list(report, rows):
    result = report.calculate(rows)
    headers = report.headers()
    return [dict(zip(headers, r)) for r in result]


def test_performance_report():
    rows = [
        {"position": "Backend", "performance": "4.0"},
        {"position": "Backend", "performance": "5.0"},
        {"position": "DevOps", "performance": "4.9"},
    ]

    report = PerformanceReport()
    result_dicts = to_dict_list(report, rows)

    assert len(result_dicts) == 2
    assert result_dicts[0]["position"] == "DevOps"
    assert result_dicts[0]["avg_performance"] == 4.9

    assert result_dicts[1]["position"] == "Backend"
    assert result_dicts[1]["avg_performance"] == 4.5
