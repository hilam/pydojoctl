from rich.layout import Layout

from pydojoctl.views.header import header


def basic_layout() -> Layout:
    layout = Layout(name='root')

    layout.split(
        Layout(name='header', size=3),
        Layout(name='main', ratio=1),
        Layout(name='footer', size=7),
    )

    layout['header'].update(header('Acompanhamento do Evento'))

    return layout


def dojo_layout() -> Layout:
    layout = basic_layout()

    layout['main'].split_row(
        Layout(name='participantes'),
        Layout(name='corpo', ratio=2, minimum_size=60),
    )

    layout['corpo'].split_column(
        Layout(name='timer', ratio=2),
        Layout(name='atuacao', ratio=8),
    )

    layout['participantes'].split(Layout(name='lista'), Layout(name='menu'))

    return layout
