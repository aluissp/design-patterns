from builders.builder import Builder
from cars import car_type
from components import Engine, Gps, TripComputer, transmissions


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def construct_sports_car(self) -> None:
        self.builder.set_car_type(car_type[1])
        self.builder.set_seats(2)
        self.builder.set_engine(Engine(3.0, 0))
        self.builder.set_transmision(transmissions[-1])
        self.builder.set_trip_computer(TripComputer())
        self.builder.set_gps(Gps())

    def construct_city_car(self) -> None:
        self.builder.set_car_type(car_type[0])
        self.builder.set_seats(4)
        self.builder.set_engine(Engine(1.2, 9))
        self.builder.set_transmision(transmissions[2])
        self.builder.set_trip_computer(TripComputer())
        self.builder.set_gps(Gps())

    def construct_suv_car(self) -> None:
        self.builder.set_car_type(car_type[2])
        self.builder.set_seats(6)
        self.builder.set_engine(Engine(2.5, 0))
        self.builder.set_transmision(transmissions[1])
        self.builder.set_gps(Gps())

    # Manuals
    def construct_sport_car_manual(self) -> None:
        self.construct_city_car()

    def construct_city_car_manual(self) -> None:
        self.construct_city_car()

    def construct_suv_car_manual(self) -> None:
        self.construct_suv_car()
