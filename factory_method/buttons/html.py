from . import Button


class HtmlButton(Button):

    def render(self):
        print('Renderizado desde html')

    def on_click(self, callback):
        callback('on click html')
