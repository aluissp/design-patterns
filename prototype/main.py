from copy import copy, deepcopy
from components import Circle, Rectangle


def main():
    circle = Circle(4, 5, 3.24)
    rectangle = Rectangle(6, 3, 2.2, 4.4)

    circle.get_shape_info()
    rectangle.get_shape_info()

    copy_circle = copy(circle)
    print(circle, copy_circle)

    copy_rectangle = deepcopy(rectangle)
    print(rectangle, copy_rectangle)


if __name__ == "__main__":
    main()
