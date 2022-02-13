import typer
from rich.console import Console
from rich.progress import track
from rich.prompt import IntPrompt, Prompt, Confirm

from service.database import criar_base
from views.header import header

app = typer.Typer()
console = Console()


@app.command()
def init():

    console.clear()

    console.print(header())
    console.print()

    console.rule("Criação da base de dados")
    criar = Confirm.ask("Confirma", choices=['s', 'n'], default='s')
    if criar == 'n':
        return

    console.rule("Aguarde")

    for n in track([1], description="Processando..."):
        criar_base()

    console.rule("Resultado")
    typer.echo(f"Base de dados criada!")

if __name__ == "__main__":
    app()
