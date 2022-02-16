from dataclasses import dataclass
from typing import Optional


@dataclass()
class Evento:
    id: Optional[int]
    nome: str
    data: str
    duracao_prevista: int
    duracao_real: Optional[int]
    ativo: Optional[int]


@dataclass()
class Participante:
    id: Optional[int]
    nome: str
    email: str
    presente: Optional[int]


@dataclass()
class EventoAtuacao:
    id: Optional[int]
    evento: Evento
    participante: Participante
    ordem_sorteio: Optional[int]


@dataclass()
class EventoConfiguracao:
    id: Optional[int]
    evento: Evento
    tempo_piloto: int
    tempo_audiencia: int
