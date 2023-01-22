from round import RoundPeg
from square import SquarePeg


class SquarePegAdapter(RoundPeg):

    def __init__(self, peg: SquarePeg) -> None:
        self.__peg = peg

    def get_radius(self) -> float:
        half_width = self.__peg.get_width() / 2
        result = pow(pow(half_width, 2) * 2, 1/2)

        return result
