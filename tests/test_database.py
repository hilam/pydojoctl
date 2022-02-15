import sqlite3 as sql

import pytest

from service.database import criar_base


@pytest.fixture
def db():
    con = sql.connect(':memory:')
    yield con
    con.close()


def test_criar_base(db):
    with db as con:
        criar_base(con)
