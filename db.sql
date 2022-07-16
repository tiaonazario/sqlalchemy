CREATE TABLE IF NOT EXISTS filmes (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(40) UNIQUE NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano integer NOT NULL
);
INSERT INTO filmes (titulo, genero, ano)
VALUES ('Forest Gump', 'Drama', 1994)
