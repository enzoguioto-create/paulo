import sqlite3

banco = sqlite3.conect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE pesoas(nome text, idade interger, email text)")

cursor.execute("INSERT INTO pessoas VALUES ('Enzo, 40, 'guiotoenzo@gmail.com)")

banco.commit()