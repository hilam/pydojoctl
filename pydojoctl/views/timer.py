from rich.panel import Panel
from rich.text import Text


def dojo_timer() -> Panel:
    return Panel(title='Timer', renderable=Text('Aqui vai o timer....'))
