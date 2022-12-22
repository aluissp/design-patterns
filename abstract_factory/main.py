from factory import GUIFactory, WinFactory, MacFactory
from application import Application


def client_code(factory: GUIFactory):

    app = Application(factory)

    app.create_ui()
    app.paint()


if __name__ == "__main__":
    print("Client: Creating windows utilites.")
    client_code(WinFactory())

    print("\nClient: Creating mac utilites.")
    client_code(MacFactory())
