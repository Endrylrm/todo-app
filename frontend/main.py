from nicegui import ui


def root():
    dark = ui.dark_mode()
    dark.auto()


ui.run(root)
