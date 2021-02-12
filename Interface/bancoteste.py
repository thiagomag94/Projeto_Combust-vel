import sqlite3

 
x_login = input("Digite seu login: ")
cursor.execute("CREATE TABLE IF NOT EXISTS Users (nome varchar[50], login varchar[50], senha varchar[50], email varchar[50])")
cursor.execute("SELECT login FROM Users WHERE login == '"+x_login+"'")
coleta = cursor.fetchall()
print(coleta)
length = len(coleta)
if length > 0 :
    print("Login indisponível")
else:
    print("Login disponível")

    cursor.execute("INSERT INTO Users VALUES('','"+x_login+"','','')  ") 
    banco.commit()
    banco.close() 
    print("Adicionado ao banco com sucesso")
 