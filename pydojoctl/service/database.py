import sqlite3 as sql
from typing import List

from pydojoctl.models.dojo import (
    Evento,
    EventoAtuacao,
    EventoConfiguracao,
    Participante,
)


def conectar() -> sql.Connection:
    try:
        con = sql.connect('codedojo.db')
        con.row_factory = sql.Row
        con.execute('PRAGMA foreign_keys=ON')
        return con
    except sql.DatabaseError as erro:
        print(erro)
        raise


def criar_base():
    con = conectar()

    try:
        with con:
            con.execute(
                """CREATE TABLE IF NOT EXISTS evento (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome text NOT NULL, 
                  data text NOT NULL, 
                  duracao_prevista integer, 
                  duracao_real integer,
                  ativo integer
                )
            """
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise

    # Participante
    try:
        with con:
            con.execute(
                """CREATE TABLE IF NOT EXISTS participante (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome text NOT NULL, 
                  email text NOT NULL,
                  presente integer
                )
            """
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise

    # Configuração do evento
    try:
        with con:
            con.execute(
                """CREATE TABLE IF NOT EXISTS evento_config (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  evento integer NOT NULL, 
                  tempo_piloto integer NOT NULL,
                  tempo_audiencia integer NOT NULL,
                  FOREIGN KEY(evento) REFERENCES evento(id)
                )
            """
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise

    # Atuação no evento
    try:
        with con:
            con.execute(
                """CREATE TABLE IF NOT EXISTS evento_atuacao (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  evento integer NOT NULL, 
                  participante integer NOT NULL,
                  ordem_sorteio integer,
                  FOREIGN KEY(evento) REFERENCES evento(id),
                  FOREIGN KEY(participante) REFERENCES participante(id)
                )
            """
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise


def inserir_evento(evento: Evento):
    try:
        with conectar() as con:
            con.execute(
                """INSERT into evento
                (nome, data, duracao_prevista, duracao_real, ativo)
                VALUES
                (:nome, :data, :duracao_prevista, :duracao_real, :ativo)
            """,
                (
                    evento.nome,
                    evento.data,
                    evento.duracao_prevista,
                    evento.duracao_real,
                    evento.ativo,
                ),
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise


def listar_eventos() -> List[Evento]:
    eventos = []
    try:
        with conectar() as con:
            result = con.execute('SELECT * FROM evento')
            rows = result.fetchall()
            for row in rows:
                eventos.append(Evento(**row))
    except sql.DatabaseError as erro:
        print(erro)
        raise
    return eventos


def buscar_evento(evento_id) -> Evento:
    try:
        with conectar() as con:
            result = con.execute(
                'SELECT * FROM evento where id = :evento_id',
                {'evento_id': evento_id},
            )
            row = result.fetchone()
            return Evento(**row)
    except sql.DatabaseError as erro:
        print(erro)
        raise


def inserir_participante(participante: Participante):
    try:
        with conectar() as con:
            con.execute(
                """INSERT into participante
                (nome, email, presente)
                VALUES
                (:nome, :email, :presente)
            """,
                (participante.nome, participante.email, participante.presente),
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise


def inserir_configuracao(evento_config: EventoConfiguracao):
    try:
        with conectar() as con:
            con.execute(
                """INSERT into evento_config
                (evento, tempo_piloto, tempo_audiencia)
                VALUES
                (evento, tempo_piloto, tempo_audiencia)
            """,
                (
                    evento_config.evento.id,
                    evento_config.tempo_piloto,
                    evento_config.tempo_audiencia,
                ),
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise


def inserir_atuacao(evento_atuacao: EventoAtuacao):
    try:
        with conectar() as con:
            con.execute(
                """INSERT into evento_atuacao
                (evento, participante, ordem_sorteio)
                VALUES
                (:evento, :participante, :ordem_sorteio)
            """,
                (
                    evento_atuacao.evento.id,
                    evento_atuacao.participante.id,
                    evento_atuacao.ordem_sorteio,
                ),
            )
    except sql.DatabaseError as erro:
        print(erro)
        raise
