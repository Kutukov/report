from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def calculate(self, rows: list[dict]) -> list[dict]:
        pass

    @abstractmethod
    def headers(self) -> list[str]:
        pass
