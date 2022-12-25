from director.director import Director
from builders import CarBuilder, ManualBuilder


def main():
    director = Director()
    car_builder = CarBuilder()
    manual_builder = ManualBuilder()

    # Assigning a generic builder
    director.builder = car_builder

    # Building sport car
    director.construct_sports_car()

    # Getting a specific car
    car = car_builder.product
    print(car)

    # Building city car
    director.construct_city_car()
    car = car_builder.product

    # Assigning a generic builder
    director.builder = manual_builder

    # Building city car manual
    director.construct_sport_car_manual()

    # Getting specific manual
    manual = manual_builder.product
    print('Sport Car Manual:', manual.get_manual())


if __name__ == "__main__":
    main()
