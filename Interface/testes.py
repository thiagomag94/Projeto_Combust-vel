from PyQt5 import uic, QtWidgets
import sqlite3
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from html_message import html




#escolher uma das duas funções que a aplicação oferece
def escolha_modos():
    n1 = telainicial.comboBox.currentIndex()
    print(n1)
#função de login e senha
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
        telainicial.label.setText(nome_usuario+'!')
        teladelogin.label_9.setText("") 

    else:
        teladelogin.label_9.setText("Dados de login incorretos!") 
    

 
#Seção de cadastro de usuários       
def chama_teladecadastro():
    teladelogin.label_10.setText("")
    try:
        if teladelogin.checkBox.isChecked() and teladelogin.checkBox_2.isChecked():
            teladelogin.label_10.setText("Marque somente uma opção")
        elif teladelogin.checkBox.isChecked():
            teladelogin.close()
            teladecadastro.show()
            teladelogin.label_9.setText("") 
        
        elif teladelogin.checkBox_2.isChecked():
            teladelogin.close()
            teladesenha.show()
            teladelogin.label_9.setText("") 
    except:
        teladelogin.label_10.setText("Você precisa marcar uma opção")

#função voltar para a tela anterior
def voltar():
    teladecadastro.close()
    teladesenha.close()
    teladelogin.show()
    teladesenha.label_3.setText("")
    teladesenha.label_2.setText("")
    teladelogin.lineEdit.setText("")
    teladelogin.lineEdit_2.setText("")
    teladecadastro.label_2.setText("")

def logout():
    telainicial.close()
    teladelogin.show()

def cadastrar():
    try:
        teladecadastro.label_2.setText("")
        nome_criar = teladecadastro.lineEdit.text()
        login_criar = teladecadastro.lineEdit_2.text()
        senha_criar = teladecadastro.lineEdit_3.text()
        email_criar = teladecadastro.lineEdit_5.text()
        confirmasenha_criar = teladecadastro.lineEdit_4.text()
        if senha_criar != confirmasenha_criar:
            teladecadastro.label_2.setText("As senhas são diferentes!")
        elif nome_criar != "" and login_criar != "" and senha_criar != "" and email_criar != "" and confirmasenha_criar != "" :
            banco = sqlite3.connect('primeiro_banco.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Users (nome varchar[50], login varchar[50], senha varchar[50], email varchar[50])")
            cursor.execute("SELECT login FROM Users WHERE login == '"+login_criar+"'")
            coleta = cursor.fetchall()
            print(coleta)
            length = int(len(coleta))
            if length > 0 :
                teladecadastro.label_3.setText("Login indisponível")
            else:
                cursor.execute("INSERT INTO Users VALUES('"+nome_criar+"','"+login_criar+"','"+senha_criar+"','"+email_criar+"') ") 
                teladecadastro.label_2.setText("Usuário cadastrado com sucesso.")
                banco.commit()
                banco.close()
                teladecadastro.lineEdit.setText("")
                teladecadastro.lineEdit_2.setText("")
                teladecadastro.lineEdit_3.setText("")
                teladecadastro.lineEdit_4.setText("")
                teladecadastro.lineEdit_5.setText("")


        
        else:
            teladecadastro.label_2.setText("Por favor, digite os valores")
    except:
        teladecadastro.label_2.setText("Ocorreu algum erro no cadastro.")   
def enviar_email(nomeusuario, novasenha, emailcoletado):
    host = 'smtp.gmail.com'
    port = 587
    user = 'thiagomag94@gmail.com'
    password = open('senha.txt')
    

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password.read())

    # Criando mensagem com código HTML

    email = emailcoletado[0][0]
    print(email)
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = email
    email_msg['Subject'] = 'REDEFINIÇÃO DE SENHA - sPYce Travel Assistant'
    print('Adicionando texto...')

    email_msg.attach(MIMEText(html(nomeusuario, novasenha),  _subtype= 'html'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    print('Mensagem enviada!')
    server.quit()   
    

def redef_senha():
    #criação da nova senha 
    teladesenha.label_2.setText("")
    novasenha = teladesenha.lineEdit_3.text()
    confirmasenha = teladesenha.lineEdit_4.text()
    nome_usuario = teladelogin.lineEdit.text()
    


    #comparação da senha com confirmação
    if novasenha == confirmasenha :

        #atualização do banco
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Users (nome varchar[50], login varchar[50], senha varchar[50], email[50])")
        cursor.execute("UPDATE Users SET senha = '"+novasenha+"' WHERE login = '"+nome_usuario+"'")
        banco.commit()
        banco.close()
        teladesenha.label_3.setText("A senha foi redefinida com sucesso")
        banco = sqlite3.connect('primeiro_banco.db')
        cursor = banco.cursor()
        cursor.execute("SELECT email FROM Users WHERE senha = '"+novasenha+"' and login = '"+nome_usuario+"' ") 
        email_coletado = cursor.fetchall()

        # Configuração do e-mail
        enviar_email(nome_usuario, novasenha, email_coletado)
    else :
        teladesenha.label_2.setText("As senhas não são iguais")

    teladesenha.lineEdit_3.setText("")
    teladesenha.lineEdit_4.setText("")
    

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
teladesenha.pushButton.clicked.connect(redef_senha)
telainicial.comboBox.activated.connect(escolha_modos)
telainicial.actionSair.triggered.connect(logout)


app.exec()
 
