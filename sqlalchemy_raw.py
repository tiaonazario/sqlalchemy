from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações
engine = create_engine(
    "postgresql+psycopg2://postgres:postgre@localhost:5432/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Filmes(Base):
    """Entidades"""

    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(40), nullable=False, unique=True)
    genero = Column(String(30), nullable=False, unique=True)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme (titulo={self.titulo}, ano={self.ano})"


# SQL
# Insert
data_insert = Filmes(titulo="Dracula", genero="Drama", ano=1996)
session.add(data_insert)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.id == 3).delete()
session.commit()

# Update
session.query(Filmes).filter(Filmes.id == 4).update({"ano": 1996})
session.commit()

# Select
data = session.query(Filmes).all()
print(data)

session.close()
