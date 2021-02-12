from PyQt5 import uic, QtWidgets
import sqlite3

def chama_telainicial():
    teladelogin.label_9.setText("")
    nome_usuario = teladelogin.lineEdit.text()
    senha = teladelogin.lineEdit_2.text()

    banco = sqlite3.connect('primeiro_banco.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM Users WHERE login = '"+nome_usuario+"' ")
        senha_bd = cursor.fetchall()
        banco.close()
    except:
        teladelogin.label_9.setText('Erro ao logar')
    
    if senha == senha_bd[0][0]:
        teladelogin.close()
        telainicial.show()
        telainicial.label.setText("Olá,"+nome_usuario)
    else:
        teladelogin.label_9.setText("Dados de login incorretos!") 


        
def chama_teladecadastro():
    teladelogin.label_10.setText("")
    try:
        if teladelogin.checkBox.isChecked() and teladelogin.checkBox_2.isChecked():
            teladelogin.label_10.setText("Marque somente uma opção")
        elif teladelogin.checkBox.isChecked():
            teladelogin.close()
            teladecadastro.show()
        
        elif teladelogin.checkBox_2.isChecked():
            teladelogin.close()
            teladesenha.show()
    except:
        teladelogin.label_10.setText("Você precisa marcar uma opção")
    

def voltar():
    teladecadastro.close()
    teladelogin.show()

def logout():
    telainicial.close()
    teladelogin.show()

def cadastrar():
    nome_criar = teladecadastro.lineEdit.text()
    login_criar = teladecadastro.lineEdit_2.text()
    senha_criar = teladecadastro.lineEdit_3.text()


    banco = sqlite3.connect('primeiro_banco.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (nome varchar[50], login varchar[50], senha varchar[50])")
    cursor.execute("INSERT INTO Users VALUES('"+nome_criar+"', '"+login_criar+"','"+senha_criar+"')")
    banco.commit()
    banco.close()
    teladecadastro.lineEdit.setText("")
    teladecadastro.lineEdit_2.setText("")
    teladecadastro.lineEdit_3.setText("")
    teladecadastro.lineEdit_4.setText("") 

app = QtWidgets.QApplication([])
teladelogin = uic.loadUi("teladelogin.ui")
telainicial = uic.loadUi("telainicial.ui")
teladecadastro = uic.loadUi("teladecadastro.ui")
teladesenha = uic.loadUi("teladesenha.ui")
teladelogin.pushButton_3.clicked.connect(chama_telainicial)

#preciso estudar mais para resolver esse trecho da interface com um IF
teladelogin.pushButton_2.clicked.connect(chama_teladecadastro)
teladelogin.show()
teladecadastro.pushButton.clicked.connect(cadastrar)
teladecadastro.pushButton_2.clicked.connect(voltar)
teladesenha.pushButton_2.clicked.connect(voltar)


app.exec()
 
