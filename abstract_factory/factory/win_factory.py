from . import GUIFactory
from product import Button, Checkbox, WinButton, WinCheckbox


class WinFactory(GUIFactory):

    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()
