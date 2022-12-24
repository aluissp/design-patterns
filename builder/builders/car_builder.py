from . import Builder
from cars import Car


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

    def set_seats(self, number: int) -> None:
        self._product.add('seats', number)

    def set_engine(self, engine) -> None:
        self._product.add('engine', engine)

    def set_trip_computer(self, trip_computer) -> None:
        self._product.add('trip_computer', trip_computer)

    def set_gps(self, gps) -> None:
        self._product.add('gps', gps)
