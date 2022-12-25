from . import Builder
from cars import Car
from components import Engine, Gps, TripComputer


class CarBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        product = self._product
        self.reset()
        return product

    def set_car_type(self, car_type: str) -> None:
        self._product._Car__set_car_type(car_type)

    def set_seats(self, number: int) -> None:
        self._product._Car__set_seats(number)

    def set_engine(self, engine: Engine) -> None:
        self._product._Car__set_engine(engine)

    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        self._product._Car__set_trip_computer(trip_computer)

    def set_gps(self, gps: Gps) -> None:
        self._product._Car__set_gps(gps)

    def set_transmision(self, transmission: str) -> None:
        self._product._Car__set_transmission(transmission)
