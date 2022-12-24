from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def set_seats(self, number: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self) -> None:
        pass

    @abstractmethod
    def set_gps(self) -> None:
        pass
