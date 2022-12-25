from typing import Any


class TripComputer:
    def __init__(self) -> None:
        self.__car = None

    def set_car(self, car: Any):
        self.__car = car

    def show_fue_level(self):
        print(f'Fue level: {self.__car.get_fuel()}')

    def show_status(self):
        if self.__car.get_engine().is_started():
            print('Car is started')
        else:
            print('Car is not started')
