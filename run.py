from infra.repository.atores_repository import AtoresRepository

repo = AtoresRepository()

response = repo.select()

print(response)
