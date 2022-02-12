from datetime import datetime
from typing import Optional


class Evento:
    nome: str
    data: datetime
    duracao_prevista: int
    duracao_real: Optional[int]


class Participante:
    nome: str
    email: str


class EventoAtuacao:
    evento: Evento
    participante: Participante
    ordem_sorteio: Optional[int]


class EventoConfiguracao:
    evento: Evento
    tempo_piloto: int
    tempo_audiencia: int
