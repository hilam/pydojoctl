from rich import box
from rich.align import Align
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def dojo_menu() -> Panel:
    menu_header = Text.from_markup(
        """Escolha uma das opções abaixo para continuar"""
    )

    menu_opcoes = Table.grid(padding=1)
    menu_opcoes.add_column(style='green', justify='left')
    menu_opcoes.add_row('(1) Incluir evento')
    menu_opcoes.add_row('(2) Configurar evento')
    menu_opcoes.add_row('(3) Incluir participante')
    menu_opcoes.add_row('(4) Sortear atuação')
    menu_opcoes.add_row('(5) Iniciar evento')

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(menu_header, menu_opcoes)

    message_panel = Panel(
        Align.center(
            Group(menu_header, '\n', Align.center(menu_opcoes)),
            vertical='middle',
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title='[b underline red]Opções',
        border_style='bright_blue',
    )
    return message_panel
