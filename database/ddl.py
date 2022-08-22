import sqlite3

conn = sqlite3.connect('aemotor.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_pessoa(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(30) NOT NULL,
        dt_nascimento VARCHAR NOT NULL,
        telefone VARCHAR(11) NOT NULL,
        email TEXT NOT NULL
    );
""")


cursor.execute("INSERT into tb_pessoa(nome, dt_nascimento, telefone, email) values ('Rhavy Maia Guedes', '2022-08-15', '83999991234', 'rhavy@ifpb.edu.br')")

# Save (commit) the changes
conn.commit()

conn.close()

print("Tabelas criadas com sucesso!")
