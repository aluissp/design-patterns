from typing import Any


class Car:

    def __init__(self) -> None:
        self.__parts = {}

    def add(self, part_name: str, part: Any) -> None:
        self.__parts[part_name] = part

    def list_parts(self) -> None:
        print(f"Car parts: {self.__parts}")

    def get_fuel(self):
        pass

    def get_engine(self):
        pass
