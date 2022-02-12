"""
Programa para controlar um Code Dojo Online

Funcionalidades:
----------------

1) Configuração
2) Acompanhamento

"""
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

console = Console()


def make_layout() -> Layout:
  """Define o layout."""
  layout = Layout(name="root")

  layout.split(
      Layout(name="header", size=3),
      Layout(name="main", ratio=1),
      Layout(name="footer", size=7),
  )
  layout["main"].split_row(
      Layout(name="side"),
      Layout(name="body", ratio=2, minimum_size=60),
  )
  layout["side"].split(Layout(name="box1"), Layout(name="box2"))
  return layout


def make_menu() -> Panel:
    """Some example content."""
    sponsor_message = Table.grid(padding=1)
    sponsor_message.add_column(style="green", justify="right")
    sponsor_message.add_column(no_wrap=True)
    sponsor_message.add_row(
        "PUG/PB",
        "[u blue link=https://pb.python.org.br]Site do Grupo",
    )
    sponsor_message.add_row(
        "Coding Dojo 2022 V(erão) :coffee:",
        "[u blue link=https://repl.it]https://repl.it/@PUG-PB",
    )
    sponsor_message.add_row(
        "Twitter",
        "[u blue link=https://twitter.com/pug_pb]Link",
    )
    sponsor_message.add_row(
        "Blog", "[u blue link=https://www.willmcgugan.com]https://www.willmcgugan.com"
    )

    intro_message = Text.from_markup(
        """Consider supporting my work via Github Sponsors (ask your company / organization), or buy me a coffee to say thanks. - Will McGugan"""
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(intro_message, sponsor_message)

    message_panel = Panel(
        Align.center(
            Group(intro_message, "\n", Align.center(sponsor_message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Thanks for trying out Rich!",
        border_style="bright_blue",
    )
    return message_panel


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]PUG-PB[/b] Coding Dojo Control",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_menu())
layout["box2"].update(Panel(make_menu(), border_style="green"))
layout["box1"].update(Panel(layout.tree, border_style="red"))
# layout["footer"].update()


from rich.live import Live
from time import sleep


with Live(layout, refresh_per_second=10, screen=True):
  option = 0
  while option != 4:
    sleep(0.1)
    option = input('Opção:')
