import pytest

from homework_06.base import Vehicle
from homework_06.car import Car
from homework_06.exceptions import LowFuelError, NotEnoughFuel, CargoOverload
from homework_06.plane import Plane


@pytest.fixture(scope="function")
def vehicle():
    return Vehicle(weight=1, fuel=5.5, fuel_consumption=1.5)


@pytest.fixture(scope="function")
def plane():
    return Plane(weight=1, fuel=5.5, fuel_consumption=1.5, max_cargo=3)


@pytest.fixture(scope="function")
def car():
    return Car(weight=1, fuel=5.5, fuel_consumption=1.5)


def test_start_sets_attribute():
    vehicle = Vehicle(weight=1, fuel=1, fuel_consumption=1.5)
    vehicle.start()
    assert vehicle.started


def test_start_raises_low_fuel_error():
    vehicle = Vehicle(weight=1, fuel=0, fuel_consumption=1.5)
    try:
        vehicle.start()
    except LowFuelError:
        assert True
    assert not vehicle.started


def test_move_expends_fuel(vehicle):
    vehicle.move(distance=2)
    assert vehicle.fuel == 2.5


def test_move_raises_not_enough_fuel(vehicle):
    try:
        vehicle.move(distance=5)
    except NotEnoughFuel:
        assert True
    assert vehicle.fuel == 5.5


def test_car_is_vehicle(car):
    assert isinstance(car, Vehicle)


def test_plane_is_vehicle(plane):
    assert isinstance(plane, Vehicle)


def test_plane_loads_cargo(plane):
    plane.load_cargo(cargo=3)
    assert plane.cargo == 3


def test_plane_loads_cargo_raises_on_overload(plane):
    try:
        plane.load_cargo(cargo=5)
    except CargoOverload:
        assert True
    assert plane.cargo == 0


if __name__ == "__main__":
    pytest.main(["-v"])
