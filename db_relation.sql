-- com a databe já criada
CREATE TABLE IF NOT EXISTS filmes (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(40) UNIQUE NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano integer NOT NULL
);
CREATE TABLE IF NOT EXISTS atores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL,
    titulo_filme VARCHAR(50) NOT NULL REFERENCES filmes(titulo)
);
-- INSERT INTO filmes (titulo, genero, ano)
-- VALUES ('Forest Gump', 'Drama', 1994)
-- INSERT INTO atores (nome, titulo_filme)
-- VALUES ('Tom Hanks', 'Forest Gump')
