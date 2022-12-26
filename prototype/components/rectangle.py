from copy import deepcopy
from . import Shape


class Rectangle(Shape):

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    def __copy__(self):
        # With primitives attributes is not important use copy or deepcopy methods
        # x = copy(self._Shape__x)

        new_rectangle = self.__class__(
            self._Shape__x, self._Shape__y, self.__width, self.__height
        )

        new_rectangle.__dict__.update(self.__dict__)

        return new_rectangle

    def __deepcopy__(self, memo=None):

        if memo is None:
            memo = {}

        new_rectangle = self.__class__(
            self._Shape__x, self._Shape__y, self.__width, self.__height
        )
        new_rectangle.__dict__ = deepcopy(self.__dict__, memo)

        return new_rectangle

    def get_shape_info(self) -> str:
        print(
            'Rectangle info\n'
            f'x: {self._Shape__x}, y:{self._Shape__y}\n'
            f'width: {self.__width}\n'
            f'height: {self.__height}\n'
        )
