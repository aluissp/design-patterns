from . import Dialog
from buttons import Button, WindowsButton


class WindowsDialog(Dialog):

    def create_button(self) -> Button:
        return WindowsButton()
