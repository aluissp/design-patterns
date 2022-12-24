
class Gps:

    def __init__(self, route='221b, Baker Street, London  to Scotland Yard, 8-10 Broadway, London') -> None:
        self.__route = route

    def get_route(self):
        return self.__route
