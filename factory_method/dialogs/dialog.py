from abc import ABC, abstractmethod
from buttons import Button


class Dialog(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        ok_button = self.create_button()
        ok_button.on_click(lambda message: print(message))
        ok_button.render()
