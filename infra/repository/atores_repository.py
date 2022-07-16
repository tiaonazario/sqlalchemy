from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores


class AtoresRepository:
    """Atores repository"""

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Atores).all()
            return data
