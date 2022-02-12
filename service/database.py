import sqlite3 as sql


def conectar():
    try:
        con = sql.connect('codedojo.db')
        con.row_factory = sql.Row
        return con
    except sql.DatabaseError as erro:
        print(erro)


def criar_base(con):
    # Evento
    try:
        with con:
            con.execute(
                '''CREATE TABLE IF NOT EXISTS evento
                    (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome text, 
                      data text, 
                      duracao_prevista integer, 
                      duracao_real integer
                    )
                '''
            )
    except sql.DatabaseError as erro:
        print(erro)

    # Participante
    try:
        with con:
            con.execute(
                '''CREATE TABLE IF NOT EXISTS participante
                    (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome text, 
                      email text
                    )
                  '''
            )
    except sql.DatabaseError as erro:
        print(erro)

    # Configuração do evento
    try:
        with con:
            con.execute(
                '''CREATE TABLE IF NOT EXISTS evento_config
                    (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      evento integer, 
                      tempo_piloto integer, 
                      tempo_audiencia integer
                    )
                '''
            )
    except sql.DatabaseError as erro:
        print(erro)

    # Atuação no evento
    try:
        with con:
            con.execute(
                '''CREATE TABLE IF NOT EXISTS evento_atuacao
                    (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      evento integer, 
                      participante integer,
                      ordem_sorteio integer
                    )
                '''
            )
    except sql.DatabaseError as erro:
        print(erro)


def inserir_evento(con, evento):
    # Insert a row of data
    try:
        con.execute(
            '''INSERT into evento
                (nome, data, duracao_prevista, duracao_real)
                VALUES
                (?, ?, ?, ?)
            ''', (
                evento['nome'],
                evento['data'],
                evento['duracao_prevista'],
                evento['duracao_real']
            )
        )
    except sql.DatabaseError as erro:
        print(erro)
