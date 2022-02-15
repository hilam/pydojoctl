from datetime import datetime

from rich.panel import Panel
from rich.table import Table


def header(title) -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify='left', ratio=2)
    grid.add_column(justify='center', ratio=6)
    grid.add_column(justify='right', ratio=2)
    grid.add_row(
        '[b]PUG-PB[/b] Coding Dojo Control',
        f'[b]{title}[/]',
        datetime.now().ctime().replace(':', '[blink]:[/]'),
    )
    return Panel(grid, style='white on blue')
