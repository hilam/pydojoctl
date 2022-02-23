from pydojoctl.models.dojo import Evento
from pydojoctl.service.database import inserir_evento, listar_eventos, buscar_evento


def test_inserir_evento_com_sucesso_retorna_id(db):
    evento = Evento(nome='Dojo1', data='2022-01-01T00:00:00.000', duracao_prevista=90)
    id_evento = inserir_evento(evento, db)
    assert id_evento.lastrowid == 1


def test_listar_evento_inserido_com_sucesso_retorna_nome_correto(db):
    evento = Evento(nome='Dojo1', data='2022-01-01T00:00:00.000', duracao_prevista=90)
    inserir_evento(evento, db)
    eventos = listar_eventos(db)
    assert eventos[0].nome == 'Dojo1'
    assert eventos[0].id == 1


def test_buscar_evento_inserido_com_sucesso_retorna_nome_correto(db):
    evento = Evento(nome='Dojo1', data='2022-01-01T00:00:00.000', duracao_prevista=90)
    id_evento = inserir_evento(evento, db)
    result = buscar_evento(id_evento.lastrowid, db)
    assert evento.nome == result.nome
    assert id_evento.lastrowid == result.id

