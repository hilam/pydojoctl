from rich import box
from rich.panel import Panel
from rich.table import Table


def dojo_atuacao() -> Panel:
    return Panel('Aqui vai exibir o resultado dos testes')


def lista_participantes() -> Panel:

    lista = Table.grid(padding=1)
    lista.add_column(header='Nome', style='green', justify='left')
    lista.add_column(header='E-mail', style='green', justify='left')
    lista.add_row('Hildeberto', 'hildeberto@gmail.com')
    lista.add_row('Fernando', 'fernando@gmail.com')
    lista.add_row('Elayne', 'elayne@gmail.com')

    return Panel(
        title='[b underline blue]Lista de Participantes',
        border_style='red',
        box=box.ROUNDED,
        padding=(1, 2),
        renderable=lista,
    )
