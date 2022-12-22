from . import GUIFactory
from product import Button, Checkbox, MacButton, MacCheckbox


class MacFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
