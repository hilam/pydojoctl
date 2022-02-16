"""
Programa para controlar um Code Dojo Online
"""
import typer

from command import base, eventos, participantes

app = typer.Typer()

app.add_typer(
    base.app, name='base', help='Comando para manipulação da base de dados'
)
app.add_typer(
    eventos.app, name='evento', help='Comando para manipulação de eventos'
)
app.add_typer(
    participantes.app,
    name='participante',
    help='Comando para manipulação de ' 'participantes',
)

if __name__ == '__main__':
    app()
