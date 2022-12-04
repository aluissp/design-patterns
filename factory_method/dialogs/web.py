from . import Dialog
from buttons import Button, HtmlButton


class WebDialog(Dialog):

    def create_button(self) -> Button:
        return HtmlButton()
