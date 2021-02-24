from PyQt5 import uic, QtWidgets
import sqlite3
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


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
def enviar_email(nomeusuario, novasenha):
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

    
    x = '''
            <!doctype html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width" />
                <meta http-equiv= "Content-Type" />
                <meta content= "text/html" />
                <meta charset= "UTF-8" />

                
                <title>Simple Transactional Email</title>
                <style>
                /* -------------------------------------
                    GLOBAL RESETS
                ------------------------------------- */
                
                /*All the styling goes here*/
                
                img {
                    border: none;
                    -ms-interpolation-mode: bicubic;
                    max-width: 100%; 
                }

                body {
                    background-color: #f6f6f6;
                    font-family: sans-serif;
                    -webkit-font-smoothing: antialiased;
                    font-size: 14px;
                    line-height: 1.4;
                    margin: 0;
                    padding: 0;
                    -ms-text-size-adjust: 100%;
                    -webkit-text-size-adjust: 100%; 
                }

                table {
                    border-collapse: separate;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                    width: 100%; }
                    table td {
                    font-family: sans-serif;
                    font-size: 14px;
                    vertical-align: top; 
                }

                /* -------------------------------------
                    BODY & CONTAINER
                ------------------------------------- */

                .body {
                    background-color: #f6f6f6;
                    width: 100%; 
                }

                /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
                .container {
                    display: block;
                    margin: 0 auto !important;
                    /* makes it centered */
                    max-width: 580px;
                    padding: 10px;
                    width: 580px; 
                }

                /* This should also be a block element, so that it will fill 100 of the .container */
                .content {
                    box-sizing: border-box;
                    display: block;
                    margin: 0 auto;
                    max-width: 580px;
                    padding: 10px; 
                }

                /* -------------------------------------
                    HEADER, FOOTER, MAIN
                ------------------------------------- */
                .main {
                    background: #ffffff;
                    border-radius: 3px;
                    width: 100%; 
                }

                .wrapper {
                    box-sizing: border-box;
                    padding: 20px; 
                }

                .content-block {
                    padding-bottom: 10px;
                    padding-top: 10px;
                }

                .footer {
                    clear: both;
                    margin-top: 10px;
                    text-align: center;
                    width: 100%; 
                }
                    .footer td,
                    .footer p,
                    .footer span,
                    .footer a {
                    color: #999999;
                    font-size: 12px;
                    text-align: center; 
                }

                /* -------------------------------------
                    TYPOGRAPHY
                ------------------------------------- */
                h1,
                h2,
                h3,
                h4 {
                    color: #000000;
                    font-family: sans-serif;
                    font-weight: 400;
                    line-height: 1.4;
                    margin: 0;
                    margin-bottom: 30px; 
                }

                h1 {
                    font-size: 35px;
                    font-weight: 300;
                    text-align: center;
                    text-transform: capitalize; 
                }

                p,
                ul,
                ol {
                    font-family: sans-serif;
                    font-size: 14px;
                    font-weight: normal;
                    margin: 0;
                    margin-bottom: 15px; 
                }
                    p li,
                    ul li,
                    ol li {
                    list-style-position: inside;
                    margin-left: 5px; 
                }

                a {
                    color: #3498db;
                    text-decoration: underline; 
                }

                /* -------------------------------------
                    BUTTONS
                ------------------------------------- */
                .btn {
                    box-sizing: border-box;
                    width: 100%; }
                    .btn > tbody > tr > td {
                    padding-bottom: 15px; }
                    .btn table {
                    width: auto; 
                }
                    .btn table td {
                    background-color: #ffffff;
                    border-radius: 5px;
                    text-align: center; 
                }
                    .btn a {
                    background-color: #ffffff;
                    border: solid 1px #3498db;
                    border-radius: 5px;
                    box-sizing: border-box;
                    color: #3498db;
                    cursor: pointer;
                    display: inline-block;
                    font-size: 14px;
                    font-weight: bold;
                    margin: 0;
                    padding: 12px 25px;
                    text-decoration: none;
                    text-transform: capitalize; 
                }

                .btn-primary table td {
                    background-color: #3498db; 
                }

                .btn-primary a {
                    background-color: #3498db;
                    border-color: #3498db;
                    color: #ffffff; 
                }

                /* -------------------------------------
                    OTHER STYLES THAT MIGHT BE USEFUL
                ------------------------------------- */
                .last {
                    margin-bottom: 0; 
                }

                .first {
                    margin-top: 0; 
                }

                .align-center {
                    text-align: center; 
                }

                .align-right {
                    text-align: right; 
                }

                .align-left {
                    text-align: left; 
                }

                .clear {
                    clear: both; 
                }

                .mt0 {
                    margin-top: 0; 
                }

                .mb0 {
                    margin-bottom: 0; 
                }

                .preheader {
                    color: transparent;
                    display: none;
                    height: 0;
                    max-height: 0;
                    max-width: 0;
                    opacity: 0;
                    overflow: hidden;
                    mso-hide: all;
                    visibility: hidden;
                    width: 0; 
                }

                .powered-by a {
                    text-decoration: none; 
                }

                hr {
                    border: 0;
                    border-bottom: 1px solid #f6f6f6;
                    margin: 20px 0; 
                }

                /* -------------------------------------
                    RESPONSIVE AND MOBILE FRIENDLY STYLES
                ------------------------------------- */
                @media only screen and (max-width: 620px) {
                    table[class=body] h1 {
                    font-size: 28px !important;
                    margin-bottom: 10px !important; 
                    }
                    table[class=body] p,
                    table[class=body] ul,
                    table[class=body] ol,
                    table[class=body] td,
                    table[class=body] span,
                    table[class=body] a {
                    font-size: 16px !important; 
                    }
                    table[class=body] .wrapper,
                    table[class=body] .article {
                    padding: 10px !important; 
                    }
                    table[class=body] .content {
                    padding: 0 !important; 
                    }
                    table[class=body] .container {
                    padding: 0 !important;
                    width: 100% !important; 
                    }
                    table[class=body] .main {
                    border-left-width: 0 !important;
                    border-radius: 0 !important;
                    border-right-width: 0 !important; 
                    }
                    table[class=body] .btn table {
                    width: 100% !important; 
                    }
                    table[class=body] .btn a {
                    width: 100% !important; 
                    }
                    table[class=body] .img-responsive {
                    height: auto !important;
                    max-width: 100% !important;
                    width: auto !important; 
                    }
                }

                /* -------------------------------------
                    PRESERVE THESE STYLES IN THE HEAD
                ------------------------------------- */
                @media all {
                    .ExternalClass {
                    width: 100%; 
                    }
                    .ExternalClass,
                    .ExternalClass p,
                    .ExternalClass span,
                    .ExternalClass font,
                    .ExternalClass td,
                    .ExternalClass div {
                    line-height: 100%; 
                    }
                    .apple-link a {
                    color: inherit !important;
                    font-family: inherit !important;
                    font-size: inherit !important;
                    font-weight: inherit !important;
                    line-height: inherit !important;
                    text-decoration: none !important; 
                    }
                    #MessageViewBody a {
                    color: inherit;
                    text-decoration: none;
                    font-size: inherit;
                    font-family: inherit;
                    font-weight: inherit;
                    line-height: inherit;
                    }
                    .btn-primary table td:hover {
                    background-color: #34495e !important; 
                    }
                    .btn-primary a:hover {
                    background-color: #34495e !important;
                    border-color: #34495e !important; 
                    } 
                }

                </style>
            </head>
            <body class="">
                <span class="preheader"></span>
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
                <tr>
                    <td>&nbsp;</td>
                    <td class="container">
                    <div class="content">

                        <!-- START CENTERED WHITE CONTAINER -->
                        <table role="presentation" class="main">

                        <!-- START MAIN CONTENT AREA -->
                        <tr>
                            <td class="wrapper">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                <td>
                                    <p>Olá, '''+nomeusuario+'''!</p>
                                    <p>Sua nova senha é:<b>'''+novasenha+''' </b></p>
                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                                    <tbody>
                                        <tr>
                                        <td align="left">
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                            <tbody>
                                                <tr>
                                                <td> <a href="http://www.upe.br/" target="_blank">Clique aqui</a> </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                    </tbody>
                                    </table>
                                    <p>Espero que faça bom proveito desse sistema.</p>
                                    <p>Até mais!</p>
                                </td>
                                </tr>
                            </table>
                            </td>
                        </tr>

                        <!-- END MAIN CONTENT AREA -->
                        </table>
                        <!-- END CENTERED WHITE CONTAINER -->

                        <!-- START FOOTER -->
                        <div class="footer">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                            <td class="content-block">
                                <span class="apple-link">Company Inc, 3 Abbey Road, San Francisco CA 94102</span>
                                <br> Don't like these emails? <a href="http://i.imgur.com/CScmqnj.gif">Unsubscribe</a>.
                            </td>
                            </tr>
                            <tr>
                            <td class="content-block powered-by">
                                Powered by <a href="http://www.upe.br/">HTMLemail</a>.
                            </td>
                            </tr>
                        </table>
                        </div>
                        <!-- END FOOTER -->

                    </div>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                </table>
            </body>
            </html>

            '''
    email = email_coletado[0][0]
    print(email)
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user
    email_msg['To'] = email
    email_msg['Subject'] = 'REDEFINIÇÃO DE SENHA - sPYce Travel Assistant'
    print('Adicionando texto...')

    email_msg.attach(MIMEText(x,  _subtype= 'html'))

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
        enviar_email(nome_usuario, novasenha)
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
 
