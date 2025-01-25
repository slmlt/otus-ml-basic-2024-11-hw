from homework_06.base import Vehicle
from homework_06.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: float
    max_cargo: float

    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo: float):
        total = self.cargo + cargo
        if total <= self.max_cargo:
            self.cargo = total
        else:
            raise CargoOverload

    def remove_all_cargo(self) -> float:
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
