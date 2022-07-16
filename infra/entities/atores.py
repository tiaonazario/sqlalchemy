from infra.configs.base import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class Atores(Base):
    """Atores"""

    __tablename__ = "atores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    titulo_filme = Column(String(50), ForeignKey("filmes.titulo"))

    def __repr__(self):
        return f"Ator (id={self.id}, nome={self.nome}, filme={self.titulo_filme})"
