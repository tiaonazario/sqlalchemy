from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert("Thor: Amor e Trovão", "Ação", 2022)
repo.delete(5)
data = repo.select()

print(data)
