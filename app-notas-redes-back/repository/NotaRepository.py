from conection.ConectionDb import ConectionDb
from entity.Nota import Nota


class NotaRepository:
    def save(nota: Nota):
        QUERY_INSERT = """INSERT INTO notas
                          (nome, descricao, data) 
                          VALUES (?,?,?);"""

        data = (nota.nome, nota.descricao, nota.data)
        ConectionDb.persist(QUERY_INSERT, data)

    def delete(id):
        QUERY_DELETE = """DELETE FROM notas
                            WHERE id = ?;
                            """

        data = (id,)
        ConectionDb.persist(QUERY_DELETE, data)

    def update(nota: Nota):
        print(nota)
        QUERY_UPDATE = """UPDATE notas
                            SET 
                            nome = ?, 
                            descricao = ?, 
                            "data" = ?
                            WHERE id=?;"""

        data = (nota.nome, nota.descricao, nota.data, nota.id)
        ConectionDb.persist(QUERY_UPDATE, data)

    def findAll():
        QUERY_FIND_ALL = """SELECT id, nome, descricao, data FROM notas;"""
        result = ConectionDb.execute(QUERY_FIND_ALL)

        return result
