from dataclasses import dataclass
from datetime import datetime as dt
from typing import Any


@dataclass
class Weather:
    date: dt
    details: dict[Any, Any]
    temp: str
    weather: list[dict[Any, Any]]
    description: str

    def __str__(self):
        return f"[{self.date:%H:%M}] {self.temp}C° ({self.description})"
