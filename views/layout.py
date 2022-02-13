from rich.layout import Layout

from views.header import header



def evento_layout() -> Layout:
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
    )

    layout["header"].update(header())

    return layout


def basic_layout() -> Layout:
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )

    layout["header"].update(header())

    return layout


def dojo_layout() -> Layout:
    layout = basic_layout()

    layout["main"].split_row(
        Layout(name="participantes"),
        Layout(name="corpo", ratio=2, minimum_size=60)
    )

    layout["corpo"].split_column(
        Layout(name="timer", ratio=2),
        Layout(name="atuacao", ratio=8),
    )

    layout["participantes"].split(Layout(name="lista"), Layout(name="menu"))

    return layout
