from components import Engine, TripComputer, Gps


class Manual:

    def __init__(self) -> None:
        self.__car_type = None
        self.__seats = None
        self.__engine = None
        self.__transmission = None
        self.__trip_computer = None
        self.__gps = None

    def __set_car_type(self, car_type: str):
        self.__car_type = car_type

    def __set_engine(self, engine: Engine):
        self.__engine = engine

    def __set_seats(self, seats: int):
        self.__seats = seats

    def __set_transmission(self, transmission: str):
        self.__transmission = transmission

    def __set_trip_computer(self, trip_computer: TripComputer):
        self.__trip_computer = trip_computer

    def __set_gps(self, gps: Gps):
        self.__gps = gps

    def get_manual(self) -> str:
        info = f'''
        Type of car: {self.__car_type}
        Count of seats: {self.__seats}
        Engine: mielage - {self.__engine.get_mileage()}; volume - {self.__engine.get_volume()}
        Transmission: {self.__transmission}
        {'Trip Computer: Functional' if self.__trip_computer else 'Trip Computer: N/A' }
        {'GPS Navigator: Functional' if self.__gps else 'Trip Computer: N/A' }
        '''
        return info
