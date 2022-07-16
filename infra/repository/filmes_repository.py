from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:
    """Fimes repository"""

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def select_genero(self, genero: str):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(
                    Filmes.genero == genero).all()
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            return data

    def insert(self, titulo: str, genero: str, ano: int) -> None:
        with DBConnectionHandler() as db:
            try:
                data = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, id: int) -> None:
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.id == id).delete()
            db.session.commit()

    def update(self, id: int, titulo: str, genero: str, ano: int) -> None:
        with DBConnectionHandler() as db:
            data = {
                "titulo": titulo,
                "genero": genero,
                "ano": ano,
            }
            db.session.query(Filmes).filter(Filmes.id == id).update(data)
            db.session.commit()
