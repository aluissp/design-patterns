from dialogs import Dialog, WindowsDialog, WebDialog


def client_code(dialog: Dialog) -> None:
    dialog.render()


if __name__ == "__main__":
    print("App: Windows")
    client_code(WindowsDialog())
    print("\n")

    print("App: Web")
    client_code(WebDialog())
