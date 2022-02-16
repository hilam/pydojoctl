import typer
from rich.console import Console
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

from pydojoctl.models.dojo import Evento, EventoConfiguracao
from pydojoctl.service.database import (
    buscar_evento,
    inserir_configuracao,
    inserir_evento,
    listar_eventos,
)
from pydojoctl.views.header import header

app = typer.Typer()
console = Console()


def inicio(titulo):
    console.clear()
    console.print()
    console.print(header(titulo))
    console.print()


@app.command()
def create():
    inicio('Criação de evento')
    console.rule('Dados do evento')
    nome = Prompt.ask('Nome')
    console.print()
    data = Prompt.ask('Data (DD/MM/AAAA)')
    console.print()
    duracao_prevista = Prompt.ask('Duração prevista (min)')
    console.print()

    console.rule('Resultado')
    try:
        evento = Evento(
            id=None,
            nome=nome,
            data=data,
            duracao_prevista=int(duracao_prevista),
            duracao_real=0,
            ativo=0,
        )
        inserir_evento(evento)
        console.print(
            f'Evento [b]{nome}[/] em [b]{data}[/], com duração de [b]{duracao_prevista}min[/], '
            f'[u]criado com sucesso[/]!'
        )
        console.print()
        console.input('Tecle ENTER para continuar')
    except Exception as erro:
        console.print(f'[u]Erro na criação do Evento [b]{nome}[/]')
        console.print(f'[red bold]{erro}[/]')
        raise typer.Exit()
    show()


@app.command()
def show():
    inicio('Lista de eventos')
    eventos = listar_eventos()

    grid = Table(expand=True)
    grid.add_column('ID', ratio=1)
    grid.add_column('Nome', ratio=3)
    grid.add_column('Data', ratio=2)
    grid.add_column('Duração Prevista', ratio=2)
    grid.add_column('Duração Real', ratio=1)
    grid.add_column('Ativo', ratio=1)

    for evento in eventos:
        grid.add_row(
            str(evento.id),
            evento.nome,
            evento.data,
            str(evento.duracao_prevista),
            evento.duracao_real,
            evento.ativo,
        )

    console.print(grid)


@app.command()
def config(evento: str, tempo_piloto: int, tempo_audiencia: int):
    inicio('Configuração de evento')
    show()
    evento_id = IntPrompt('ID do evento')
    console.print()

    try:
        evento = buscar_evento(evento_id)
    except Exception as erro:
        console.print(f'[u]Erro na busca do Evento [b]{evento_id}[/]')
        console.print(f'[red bold]{erro}[/]')
        raise typer.Exit()

    console.rule('Configuração')
    tempo_piloto = Prompt.ask('Tempo do piloto (min)')
    console.print()
    tempo_audiencia = Prompt.ask('Tempo da audiência (min)')
    console.print()

    console.rule('Resultado')
    try:
        evento_config = EventoConfiguracao(
            id=None,
            evento=evento,
            tempo_piloto=int(tempo_piloto),
            tempo_audiencia=int(tempo_audiencia),
        )
        inserir_configuracao(evento_config)
        console.print(f'Evento [b]{id}[/] [u]configurado com sucesso[/]!')
        console.print()
        console.input('Tecle ENTER para continuar')
    except Exception as erro:
        console.print(f'[u]Erro na configuração do Evento [b]{evento.nome}[/]')
        console.print(f'[red bold]{erro}[/]')
        raise typer.Exit()


@app.command()
def start(evento: str):
    # layout = dojo_layout()
    # with Live(console=console, layout=layout, screen=True, refresh_per_second=4):
    #     inicio("")
    typer.echo(f'Iniciando: {evento}')


if __name__ == '__main__':
    app()
