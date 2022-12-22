from factory import GUIFactory


class Application:

    def __init__(self, factory: GUIFactory) -> None:
        self.__factory = factory

    def create_ui(self):
        self.__button = self.__factory.create_button()
        self.__checkbox = self.__factory.create_checkbox()

    def paint(self):
        self.__button.paint()
        self.__checkbox.paint()
