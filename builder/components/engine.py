
class Engine:

    def __init__(self, volume: float, mileage: float) -> None:
        self.__volume = volume
        self.__mileage = mileage
        self.__started = False

    def on(self):
        self.__started = True

    def off(self):
        self.__started = False

    def is_started(self):
        return self.__started

    def go(self, mileage: float):
        if self.__started:
            self.__mileage += mileage
        else:
            print('Cannot go(), you must start engine first!')

    def get_mileage(self):
        return self.__mileage

    def get_volume(self):
        return self.__volume
