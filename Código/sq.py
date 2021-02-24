import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

""" nome = input("Nome: ")

destino = input("Destino: ")

combustivel = input("combustivel")
 """
#cursor.execute("CREATE TABLE eletricidade_rota (nome text, rota text, combustivel text)")

""" cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', '"+destino+"','"+combustivel+"')")

banco.commit()  """  

cursor.execute("SELECT * from pessoas")
print(cursor.fetchall())

 