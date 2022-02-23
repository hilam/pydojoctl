from dataclasses import dataclass
from typing import Optional


@dataclass()
class Evento:
    nome: str
    data: str
    duracao_prevista: int
    id: Optional[int] = None
    duracao_real: Optional[int] = None
    ativo: Optional[int] = None


@dataclass()
class Participante:
    nome: str
    email: str
    id: Optional[int] = None
    presente: Optional[int] = None


@dataclass()
class EventoAtuacao:
    evento: Evento
    participante: Participante
    id: Optional[int] = None
    ordem_sorteio: Optional[int] = None


@dataclass()
class EventoConfiguracao:
    evento: Evento
    tempo_piloto: int
    tempo_audiencia: int
    id: Optional[int] = None
