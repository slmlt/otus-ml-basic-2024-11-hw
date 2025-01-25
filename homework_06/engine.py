from dataclasses import dataclass


@dataclass(frozen=True)
class Engine:
    volume: float
    pistons: int
