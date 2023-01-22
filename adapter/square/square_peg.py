class SquarePeg:

    def __init__(self, width: float) -> None:
        self.__width = width

    def get_width(self) -> float:
        return self.__width

    def get_square(self):
        return self.__width ** 2
