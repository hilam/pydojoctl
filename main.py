"""
Programa para controlar um Code Dojo Online
"""
import typer

from command import eventos, participantes, base

app = typer.Typer()

app.add_typer(base.app, name="base")
app.add_typer(eventos.app, name="evento")
app.add_typer(participantes.app, name="participante")

if __name__ == "__main__":
    app()
