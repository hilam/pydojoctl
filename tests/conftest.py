import pytest

from pydojoctl.service.database import criar_base, conectar


@pytest.fixture(scope="function")
def db():
    con = conectar(':memory:')
    criar_base(con)
    yield con
    con.close()
