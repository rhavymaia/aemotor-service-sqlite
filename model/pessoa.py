from database.sqlite import connect_to_db
import sqlite3


class Pessoa():
    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone


def get_pessoas():
    pessoas = []
    try:
        conn = connect_to_db()

        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = "SELECT * FROM tb_pessoa"
        cursor.execute(query)
        rows = cursor.fetchall()

        # convert row objects to dictionary
        for row in rows:
            pessoa = {}
            pessoa["id"] = row[0]
            pessoa["nome"] = row[1]
            pessoa["dt_nascimento"] = row[2]
            pessoa["telefone"] = row[3]
            pessoa["email"] = row[4]
            pessoas.append(pessoa)
    except Exception as err:
        print('Query Failed: %s\nError: %s' % (query, str(err)))
        pessoas = []
    finally:
        conn.close()
    return pessoas


def get_pessoa_id(pessoa_id):
    pessoa = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_pessoa WHERE id = ?",
                       (pessoa_id,))

        row = cursor.fetchone()

        # convert row object to dictionary
        pessoa["id"] = row["id"]
        pessoa["nome"] = row["nome"]
        pessoa["dt_nascimento"] = row["dt_nascimento"]
        pessoa["telefone"] = row["telefone"]
        pessoa["email"] = row["email"]

    except:
        pessoa = {}

    return pessoa


def insert_pessoa(pessoa):
    inserted_pessoa = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_pessoa(nome, dt_nascimento, telefone, email) VALUES(?, ?, ?, ?)",
                    (pessoa.nome, pessoa.nascimento, pessoa.telefone, pessoa.email))
        conn.commit()
        id = cur.lastrowid
        inserted_pessoa = get_pessoa_id(id)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_pessoa
