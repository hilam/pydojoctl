import typer

app = typer.Typer()


@app.command()
def criar(nome: str, email: str):
    typer.echo(f"Criando participante: {nome}, {email}")


@app.command()
def mostrar():
    typer.echo(f"Mostrando participantes")


@app.command()
def sortear():
    typer.echo(f"Sorteando ordem de participação")


if __name__ == "__main__":
    app()