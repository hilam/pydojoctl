from datetime import datetime

from rich.panel import Panel
from rich.table import Table


def header() -> Panel:
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")
    grid.add_row(
        "[b]PUG-PB[/b] Coding Dojo Control",
        datetime.now().ctime().replace(":", "[blink]:[/]"),
    )
    return Panel(grid, style="white on blue")
