from infra.configs.base import Base
from sqlalchemy import Integer, String, Column


class Filmes(Base):
    """Fimes"""

    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(40), nullable=False, unique=True)
    genero = Column(String(30), nullable=False, unique=True)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme (id={self.id}, titulo={self.titulo}, ano={self.ano})"
