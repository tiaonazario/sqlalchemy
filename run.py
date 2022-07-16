from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

response = repo.select_genero("Acão")

print(response)
