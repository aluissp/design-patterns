from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    @abstractmethod
    def get_shape_info(self) -> str:
        pass
