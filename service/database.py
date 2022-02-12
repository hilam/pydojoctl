import sqlite3 as sql

from models.dojo import Evento, Participante, EventoConfiguracao, EventoAtuacao


def conectar():
    try:
        con = sql.connect('codedojo.db')
        con.row_factory = sql.Row
        con.execute("PRAGMA foreign_keys=ON")
        return con
    except sql.DatabaseError as erro:
        print(erro)


def criar_base(con):
    # Evento
    try:
        with con:
            con.execute('''CREATE TABLE IF NOT EXISTS evento (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome text NOT NULL, 
                  data text NOT NULL, 
                  duracao_prevista integer, 
                  duracao_real integer,
                  ativo integer
                )
            ''')
    except sql.DatabaseError as erro:
        print(erro)

    # Participante
    try:
        with con:
            con.execute('''CREATE TABLE IF NOT EXISTS participante (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome text NOT NULL, 
                  email text NOT NULL,
                  presente integer
                )
            ''')
    except sql.DatabaseError as erro:
        print(erro)

    # Configuração do evento
    try:
        with con:
            con.execute('''CREATE TABLE IF NOT EXISTS evento_config (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  evento integer NOT NULL, 
                  tempo_piloto integer NOT NULL,
                  tempo_audiencia integer NOT NULL,
                  FOREIGN KEY(evento) REFERENCES evento(id)
                )
            ''')
    except sql.DatabaseError as erro:
        print(erro)

    # Atuação no evento
    try:
        with con:
            con.execute('''CREATE TABLE IF NOT EXISTS evento_atuacao (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  evento integer NOT NULL, 
                  participante integer NOT NULL,
                  ordem_sorteio integer,
                  FOREIGN KEY(evento) REFERENCES evento(id),
                  FOREIGN KEY(participante) REFERENCES participante(id)
                )
            ''')
    except sql.DatabaseError as erro:
        print(erro)


def inserir_evento(con, evento: Evento):
    try:
        con.execute('''INSERT into evento
            (nome, data, duracao_prevista, duracao_real, ativo)
            VALUES
            (:nome, :data, :duracao_prevista, :duracao_real, :ativo)
        ''', evento)
    except sql.DatabaseError as erro:
        print(erro)


def inserir_participante(con, participante: Participante):
    try:
        con.execute('''INSERT into participante
            (nome, email, presente)
            VALUES
            (:nome, :email, :presente)
        ''', participante)
    except sql.DatabaseError as erro:
        print(erro)


def inserir_configuracao(con, evento_config: EventoConfiguracao):
    try:
        con.execute('''INSERT into evento_config
            (evento, tempo_piloto, tempo_audiencia)
            VALUES
            (evento, tempo_piloto, tempo_audiencia)
        ''', evento_config)
    except sql.DatabaseError as erro:
        print(erro)


def inserir_atuacao(con, evento_atuacao: EventoAtuacao):
    try:
        con.execute('''INSERT into evento_atuacao
            (evento, participante, ordem_sorteio)
            VALUES
            (:evento, :participante, :ordem_sorteio)
        ''', evento_atuacao)
    except sql.DatabaseError as erro:
        print(erro)
