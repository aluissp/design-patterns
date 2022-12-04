from . import Button


class WindowsButton(Button):

    def render(self):
        print('Renderizado desde windows')

    def on_click(self, callback: callable):
        callback('on click windows')
