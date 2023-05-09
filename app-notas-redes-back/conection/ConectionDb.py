import sqlite3
from config.Config import Config


class ConectionDb():

    def initialize(self):
        config = Config()
        print("CRIANDO DATABASE ("+config.getDatabaseName()+")")
        conn = sqlite3.connect(config.getDatabaseName())
        cursor = conn.cursor()
        sql = [
            """            
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT NOT NULL,
                data DATE
            );
            """,
        ]

        for s in sql:
            cursor.execute(s)
        print('Tabelas geradas com sucesso')
        conn.close()

    def persist(sql, data):
        try:
            config = Config()
            sqliteConnection = sqlite3.connect(config.getDatabaseName())
            cursor = sqliteConnection.cursor()
            print("Sucesso ao conectar com o banco")

            cursor.execute(sql, data)
            sqliteConnection.commit()
            print("Query executada com sucesso")

            cursor.close()

        except sqlite3.Error as error:
            print("Falha ao inserir dado ao sqlite: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Conexão fechada com o banco")

    def execute(query):
        records = None
        try:
            config = Config()
            sqliteConnection = sqlite3.connect(config.getDatabaseName())
            cursor = sqliteConnection.cursor()
            print("Conectando ao sqlite")

            cursor.execute(query)

            records = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Falha ao ler a tabela: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Conexão com o banco fechada")
            return records
