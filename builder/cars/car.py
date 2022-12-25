from typing import Any
from components import Engine, Gps, TripComputer


class Car:

    def __init__(self) -> None:
        self.__car_type = None
        self.__seats = None
        self.__engine = None
        self.__transmission = None
        self.__trip_computer = None
        self.__gps = None
        self.__fuel = None

    def __set_car_type(self, car_type: str):
        self.__car_type = car_type

    def get_car_type(self) -> str:
        return self.__car_type

    def __set_engine(self, engine: Engine):
        self.__engine = engine

    def get_engine(self) -> Engine:
        return self.__engine

    def set_fuel(self, fuel: float):
        self.__fuel = fuel

    def get_fuel(self) -> float:
        return self.__fuel

    def __set_seats(self, seats: int):
        self.__seats = seats

    def get_seats(self) -> int:
        return self.__seats

    def __set_transmission(self, transmission: str):
        self.__transmission = transmission

    def get_transmission(self) -> str:
        return self.__transmission

    def __set_trip_computer(self, trip_computer: TripComputer):
        self.__trip_computer = trip_computer
        self.__trip_computer.set_car(self)

    def get_trip_computer(self):
        return self.__trip_computer

    def __set_gps(self, gps: Gps):
        self.__gps = gps

    def get_gps(self):
        return self.__gps
