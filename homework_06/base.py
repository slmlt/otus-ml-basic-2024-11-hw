from abc import ABC

from homework_06 import exceptions


class Vehicle(ABC):
    weight: float
    started: bool
    fuel: float
    fuel_consumption: float

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        super().__init__()
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: float):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel = self.fuel - fuel_needed
        else:
            raise exceptions.NotEnoughFuel
        return True
