from repository.NotaRepository import NotaRepository
from entity.Nota import Nota


class NotaService:
    def save(nota):
        NotaRepository.save(nota)

    def editar(nota):
        NotaRepository.update(nota)

    def deletar(id):
        NotaRepository.delete(id)

    def findAll():
        result = NotaRepository.findAll()
        notas = []
        if type(result) is list:
            for row in result:
                nota = Nota(
                    id=row[0],
                    nome=row[1],
                    descricao=row[2],
                    data=row[3]
                )

                notas.append(nota)

        return notas
