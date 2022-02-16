import typer
from rich.console import Console
from rich.progress import track
from rich.prompt import Confirm

from service.database import criar_base
from views.header import header

app = typer.Typer()
console = Console()


@app.command()
def init():

    console.clear()
    console.print()
    console.print(header('Criação da base de dados'))
    console.print()

    console.rule('Confirmação')
    console.print()
    criar = Confirm.ask('Confirma', choices=['s', 'n'], default='s')
    if criar == 'n':
        return

    console.print()
    console.rule('Aguarde')
    console.print()

    for _ in track([1], description='Processando...'):
        criar_base()

    console.print()
    console.rule('Resultado')
    console.print()
    console.print('[b]Base de dados [u]criada com sucesso[/]!')


if __name__ == '__main__':
    app()
