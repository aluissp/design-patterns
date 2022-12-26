from copy import deepcopy
from . import Shape


class Circle(Shape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.__radius = radius

    def __copy__(self):
        # With primitives attributes is not important use copy or deepcopy methods
        # x = copy(self._Shape__x)

        new_circle = self.__class__(
            self._Shape__x, self._Shape__y, self.__radius
        )

        new_circle.__dict__.update(self.__dict__)

        return new_circle

    def __deepcopy__(self, memo=None):

        if memo is None:
            memo = {}

        new_circle = self.__class__(
            self._Shape__x, self._Shape__y, self.__radius
        )
        new_circle.__dict__ = deepcopy(self.__dict__, memo)

        return new_circle

    def get_shape_info(self) -> str:
        print(
            'Circle info\n'
            f'x: {self._Shape__x}, y:{self._Shape__y}\n'
            f'radius: {self.__radius}\n'
        )
