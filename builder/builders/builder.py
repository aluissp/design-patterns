from abc import ABC, abstractmethod
from components import Engine, Gps, TripComputer


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_car_type(self, car_type: str) -> None:
        pass

    @abstractmethod
    def set_seats(self, number: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine: Engine) -> None:
        pass

    @abstractmethod
    def set_transmision(self, transmission: str) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        pass

    @abstractmethod
    def set_gps(self, gps: Gps) -> None:
        pass
