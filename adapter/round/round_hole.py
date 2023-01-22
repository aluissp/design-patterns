from . import RoundPeg


class RoundHole:

    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()
