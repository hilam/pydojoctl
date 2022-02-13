import typer
from rich.console import Console
from rich.prompt import IntPrompt, Prompt

from views.header import header

app = typer.Typer()
console = Console()


@app.command()
def create():

    console.clear()

    console.print(header())
    console.print()

    console.rule("Nome do evento")
    nome = Prompt.ask()
    console.print()

    console.rule("Data")
    data = Prompt.ask()
    console.print()

    console.rule("Duração prevista (min)")
    duracao_prevista = Prompt.ask()
    console.print()

    console.rule("Resultado")
    typer.echo(f"Evento: {nome} em {data}, com duração de {duracao_prevista}min criado!")


@app.command()
def show():
    typer.echo(f"Mostrando eventos")


@app.command()
def start(evento: str):
    typer.echo(f"Iniciando: {evento}")


@app.command()
def config(evento: str, tempo_piloto: int, tempo_audiencia: int):
    console.print(header())
    IntPrompt()
    typer.echo(
        f"Configurando {evento} com {tempo_piloto}min para piloto e {tempo_audiencia}min para "
        f"audiência"
    )


if __name__ == "__main__":
    app()
