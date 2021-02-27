import time
import sys
from time import sleep
import sqlite3
from os import system
#conectar com banco de dados
def banco():
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, destino text, combustivel text)")

    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', '"+nome_cidade+"','"+combustivel+"')")
    banco.commit()
    banco.close()


#Definição de funções
#linha de layout

def lin2(msg):
    print("-"*75)
    print(msg)
    print("-"*75)

def lin():
    print("-"*75)

#efeito digitação
def digitação(words):
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

#contadores auxiliares
cont= 's'
cont2= 1
cont3= '1'

#códigos ANSI de cores
RED   = "\033[1;31m"
RESET = "\033[0;0m"


def ajuda():

    c = 1
    while c == 1:
        var_ajuda = input(RESET+'Deseja obter ajuda? (s/n)  ')
        if var_ajuda.lower() == 's':
            
            digitação('\nAJUDA:\nA opção (1) é indicada para quem já sabe a distância que quer percorrer\ne deseja saber quanto custará a viagem em combustível.\nTambém é indicada para quem precisa saber se a quantidade de combustível\njá existente vai ser suficiente para percorrer todo o trajeto.\n\n')
            digitação('A opção (2) é indicada para quem só precisa saber quantos quilômetros\npode rodar com determinado valor em dinheiro.\n')
            digitação('\nOk, Vamos continuar...\n')
            c += 1
        elif var_ajuda.lower() == 'n':

            digitação('\nOk, Vamos continuar...\n')
            c += 1
        else:
            print(RED +"Você não digitou uma opção válida\n")
            c == 1     
def chamar(self):
    c = 1
    while c == 1:
        self.x = input(RESET+'Escolha entre as opções acima qual deseja utilizar(1/2):  ')
        if self.x != '1' and self.x != '2':
            print(RED +"Você não digitou uma opção válida\n")
            c == 1  
        if self.x == '1' or self.x == '2':
            c += 1

while cont == 's':
    time.sleep(1)
    #mostrar menu
    print("""
-------------------------------------------------------------------
                        MENU DE OPÇÕES
-------------------------------------------------------------------
*       [1] = Planeje sua viagem                                  *
*                                                                 *
*                                                                 *
*       [2] = Calcule quantos km conseguirá percorrer com R$      *
*                                                                 *
*                                                                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """)
 
    ajuda()

    
    #lógica do menu e interação com o usuário
    time.sleep(1)
    c = 1
    #laço_opção inválida
    while c == 1:
        opcao = input(RESET+'Escolha entre as opções acima qual deseja utilizar(1/2):  ')
        if  opcao != '1' and opcao != '2':
            print(RED +"Você não digitou uma opção válida\n")
            c == 1  
        if opcao == '1' or opcao == '2':
            c += 1
    variavel_central = opcao

    system('cls')
    #assistente virtual
        
    digitação('\nQual o seu nome? ')
    nome = input()
    system('cls')
    lin()
    #implementando um laço para não repetir a assistente virtual.
    if cont2 == 1:
        digitação('Olá, {}. Tudo bem? sou a assistente virtual do sPyce Travel. \nTe ajudarei a planejar sua viagem..\nVamos lá?\n'.format(nome))
        lin()
        time.sleep(1.5)
    system('cls')
    lin2('aguarde...')
    time.sleep(1.5)
    print('')
    system('cls')
    if variavel_central == '1':

        print("""
-------------------------------------------------------
    sPyce Travel Assistant - seu planejador de viagens
-------------------------------------------------------
    """)
        time.sleep(1.5)
        
        #seção de obtenção e processamento interno dos dados obtidos
        try:
            digitação('Qual o combustível prefere utilizar?\n')
            time.sleep(1)
            print("""
[1] = Gasolina
[2] = Álcool
[3] = Eletricidade
    
    """)
            combustivel = input('Digite por extenso:')
            system('cls')
            if combustivel.lower().strip() == 'eletricidade' :
                
                digitação("\nEscolha dentre as opções de trajeto abaixo:\n")
                time.sleep(0.7)
                opcao = (input('1)Duas cidades [ida e volta]\n2)Rota pré calculada\n'))

                if opcao.lower().strip() == 'duas cidades' or opcao.strip() == '1':
                    lin2('TRAJETO ENTRE DUAS CIDADES')

                    nome_cidade = input("Qual a cidade de destino? ")
                    autonomia_elet = float(input('Quantos Km/carga faz seu veículo elétrico? '))
                    distancia = float(input('Qual a distancia em Km entre as duas cidades? '))
                    carga_preco = float(input('Qual o preço médio por carga? '))
                    
                    vtanque = 1
                    distancia_iv = 2*distancia
                    carga_consumida = distancia_iv/autonomia_elet
                    resto = (distancia_iv % autonomia_elet)
                    parte_inteira = int(carga_consumida)
                    carga_restante= resto*100/autonomia_elet
                    parte_decimal = resto/autonomia_elet
                    custo_elet = carga_preco*carga_consumida
                    lin()

                    banco()
                    system('cls')
                    if distancia_iv==autonomia_elet:
                        digitação('Você precisará carregar a bateria totalmente apenas uma vez\n')
                    if distancia_iv < autonomia_elet:
                        digitação('Você consumirá {}% de sua carga total para percorrer o trajeto completo (ida e volta)\n'.format(carga_consumida*100))
                        digitação("Custo com energia elétrica: R$ {}\n".format(custo_elet))
                    if distancia_iv > autonomia_elet:
                        if resto ==0:
                            digitação('Você terá que recarregar {}x para completar o trajeto\n'.format(parte_inteira))
                            digitação("Custo com energia elétrica: R$ {:.2f}\n".format(custo_elet))
                        if parte_inteira >=1 and resto!=0:
                            digitação('Você terá que recarregar a bateria completamente {}x e mais {:.2f}% para completar o trajeto ida e volta\n'.format(parte_inteira,carga_restante))
                            digitação("Custo com energia elétrica: R$ {:.2f}\n".format(custo_elet))
                    system('cls')
                elif opcao.strip().lower() == "Rota calculada" or opcao.strip() == '2':

                    lin2('ROTA COMPLETA PRÉ CALCULADA')

                    nome_cidade = input("Qual a cidade de destino? ")
                    autonomia_elet = float(input('Quantos Km/carga faz seu veículo elétrico? '))
                    distancia = float(input('Qual o tamanho da rota em km ? '))
                    carga_preco = float(input('Qual o preço médio por carga? '))
                    print('Aguarde...Calculando......')
                    time.sleep(2)
                    system('cls')
                    vtanque = 1
                    distancia_iv =  distancia
                    carga_consumida = distancia_iv / autonomia_elet
                    resto = (distancia_iv % autonomia_elet)
                    parte_inteira = int(carga_consumida)
                    carga_restante = resto * 100 / autonomia_elet
                    parte_decimal = resto / autonomia_elet
                    
                    banco()
                               
                    lin()

                    if distancia_iv==autonomia_elet:
                        print('Você precisará carregar a bateria totalmente apenas uma vez\n')
                        time.sleep(1)
                    if distancia_iv < autonomia_elet:
                        print('Você consumirá {}% de sua carga total para percorrer o trajeto completo.\n'.format(carga_consumida*100))
                        time.sleep(1)
                        print("Custo com energia elétrica: R$ {:.2f}\n".format(carga_preco*carga_consumida))
                        time.sleep(1)
                    if distancia_iv > autonomia_elet:
                        if resto ==0:
                            print('Você terá que recarregar {}x para completar o trajeto\n'.format(parte_inteira))
                            time.sleep(1)
                            print("Custo com energia elétrica: R$ {:.2f}\n".format(carga_preco * carga_consumida))
                            time.sleep(1)
                        if parte_inteira >=1 and resto!=0:
                            digitação('Você terá que recarregar a bateria completamente {}x e mais {:.2f}% para completar o trajeto ida e volta '.format(parte_inteira,carga_restante))
                            time.sleep(1)
                            digitação("\nCusto com energia elétrica: R$ {:.2f}\n".format(carga_preco * (carga_consumida)))
                    time.sleep(0.5)
                    lin()
                    system('cls')
            elif combustivel.strip().lower() == 'gasolina'  or combustivel.strip().lower() == 'álcool':
                #PARTE 2
                system('cls')
                nome_cidade = input("Qual a cidade de destino? ")
                distancia = float(input('\nQual a distancia (Km) entre o ponto de partida e o destino? '))
                time.sleep(0.5)
                autonomia = float(input('\nQuantos Km/L faz seu veículo? '))
                time.sleep(0.5)
                vtanque = float(input('\nQual o volume total do tanque de combustível? '))
                time.sleep(0.5)
                combustivel_preco = float(input('\nQual o preço médio por litro de combustível? '))
                print('')

               

                # distância que o veículo percorrerá até esvaziar o tanque
                dtc = autonomia * vtanque

                #quantidade de litros a abastecer por km rodado
                comb_abastecer = distancia/autonomia


                #quantidade excedente de combustível a ser utilizado na viagem de volta (para dtc>distancia)
                comb_exc = (dtc - distancia)/autonomia

            
                divisao = distancia / (dtc)
                resto = int(distancia % dtc)
                parte_inteira = int(divisao)
                #quantidade excedente de combustível a ser utilizado na viagem de volta (para distancia>dtc)
                comb2_exc = (distancia-dtc*parte_inteira)/autonomia
                #distancia ida e volta
                distancia_iv= distancia*2
                divisao2 = distancia_iv / (dtc)
                resto2 = int(distancia_iv % dtc)
                parte_inteira2 = int(divisao2)
                comb2_exc2 = (distancia_iv - (dtc * parte_inteira2)) / autonomia
                comb_abastecer2 = distancia_iv / autonomia

                

                system('cls')
                print('')
                digitação('Seu veículo faz {:.2f} Km com {:.2f} L de {} \n'.format(dtc, vtanque, combustivel.strip()))
                time.sleep(1)
                lin()
                time.sleep(1)
                # pergunta se quer calcular para ida e volta ou só ida
                condicao1 = input("Escolha o trajeto:\n1)Somente ida\n2)Ida e volta\n3)Rota pré calculada\n")
                lin()
                time.sleep(0.5)
                #somente ida
                system('cls')
                if condicao1=='1':
                    banco()
                    
                    if distancia==dtc:
                        digitação("Você precisará encher o tanque uma vez durante o trajeto de ida")
                        time.sleep(1)
                        digitação("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(),combustivel_preco*vtanque))                    
                        lin()
                        time.sleep(1)
                    if distancia<dtc:
                        digitação("Você precisará abastecer o tanque com {:.2f} litros ou encher o tanque uma vez durante o trajeto de ida\nCaso opte por encher o tanque, sobrarão {:.2f} litros para fazer {:.2f} km na viagem de volta.\n".format(comb_abastecer,comb_exc,(dtc-distancia)))
                        lin()
                        time.sleep(1)
                        digitação("O custo total com {} sem encher o tanque: R$ {:.2f}\n".format(combustivel.strip(),comb_abastecer*combustivel_preco))
                        time.sleep(1)
                        digitação("O custo total caso deseje encher o tanque: R$ {:.2f}\n".format(vtanque*combustivel_preco))
                        lin()
                    if distancia>dtc:
                        #divisão exata (enche o tanque mais de uma vez)
                        if resto==0:
                            digitação("\nVocê precisará encher o tanque {} vezes durante o trajeto de ida\n".format(parte_inteira))
                            time.sleep(1)
                            digitação("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(), combustivel_preco * vtanque*parte_inteira))
                            time.sleep(1)
                        if parte_inteira == 1:
                            digitação("\nVocê precisará encher o tanque {} vez e encher mais {:.2f} litros para completar o trajeto de ida.\n".format(parte_inteira,comb2_exc))
                            time.sleep(1)
                            digitação("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(), combustivel_preco *(vtanque *parte_inteira+comb2_exc)))
                            lin()
                            time.sleep(1)
                        if parte_inteira>1 and resto!=0:
                            digitação("\nVocê precisará encher o tanque {} vezes e encher mais {:.2f} litros para completar o trajeto de ida.".format(parte_inteira, comb2_exc))
                            time.sleep(1)
                            digitação("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(),combustivel_preco * ((vtanque * parte_inteira) + comb2_exc)))
                            lin()
                            time.sleep(1)
                    
                if condicao1=='2':
                    banco()

                    if distancia_iv == dtc:
                            print("Você precisará encher o tanque uma vez para completar o trajeto desejado")
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}".format(combustivel.strip(), combustivel_preco * vtanque))
                            lin()
                            time.sleep(1)
                    if distancia_iv<dtc:
                        print("Você precisará abastecer o tanque com {:.2f} litros ou encher o tanque uma vez durante o trajeto \nCaso opte por encher o tanque, sobrarão {:.2f} litros para fazer {:.2f} km em outra viagem.".format(comb_abastecer2,vtanque-comb_abastecer2,(dtc-distancia_iv)))
                        lin()
                        time.sleep(1)
                        print("O custo total com {} sem encher o tanque: R$ {:.2f}".format(combustivel.strip(),comb_abastecer2*combustivel_preco))
                        time.sleep(1)
                        print("O custo total caso deseje encher o tanque: R$ {:.2f}".format(vtanque*combustivel_preco))
                        lin()
                        time.sleep(1)
                    if distancia_iv>dtc:
                        #divisão exata (enche o tanque mais de uma vez)
                        if resto2==0:
                            print("\nVocê precisará encher o tanque {} vezes para percorrer o trajeto desejado de {}km".format(parte_inteira2,distancia_iv))
                            time.sleep(1)
                            print("total de combustível gasto: {:.2f} litros".format(parte_inteira2*vtanque))
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}".format(combustivel.strip(), combustivel_preco * vtanque*parte_inteira2))
                            time.sleep(1)
                        if parte_inteira2 == 1:
                            print("\nVocê precisará encher o tanque {} vez e encher mais {:.2f} litros para completar o trajeto desejado de {}km.".format(parte_inteira2,comb2_exc2,distancia_iv))
                            time.sleep(1)
                            print("Total de combustível gasto: {:.2f} litros".format(vtanque+comb2_exc2))
                            time.sleep(1)
                            print("O custo de ida e volta com {}: R$ {:.2f}".format(combustivel.strip(), combustivel_preco *(vtanque *parte_inteira2+comb2_exc2)))
                            lin()
                            time.sleep(1)
                        if parte_inteira2>1 and resto2!=0:
                            print("\nVocê precisará encher o tanque {} vezes e encher mais {:.2f} litros para completar o trajeto de {}km.".format(parte_inteira2, comb2_exc2,distancia_iv))
                            time.sleep(1)
                            print("Total de combustível gasto: {:.2f} litros".format(parte_inteira2*vtanque+comb2_exc2))
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}".format(combustivel.strip(),combustivel_preco * ((vtanque * parte_inteira2) + comb2_exc2)))
                            lin()
                            
                    
                                                                                                                                                                                                 
                if condicao1=='3':

                    banco()
                    if distancia==dtc:
                        print("Você precisará encher o tanque uma vez durante a rota")
                        print("\nO custo total com {}: R$ {:.2f}".format(combustivel.strip(),combustivel_preco*vtanque))
                        lin()
                    if distancia<dtc:
                        print("Você precisará abastecer o tanque com {:.2f} litros ou encher o tanque uma vez durante a rota\nCaso opte por encher o tanque, sobrarão {:.2f} litros para fazer {:.2f} km em outra viagem.".format(comb_abastecer,comb_exc,(dtc-distancia)))
                        lin()
                        print("O custo total com {} sem encher o tanque: R$ {:.2f}".format(combustivel.strip(),comb_abastecer*combustivel_preco))
                        print("O custo total caso deseje encher o tanque: R$ {:.2f}".format(vtanque*combustivel_preco))
                        lin()
                    if distancia>dtc:
                        #divisão exata (enche o tanque mais de uma vez)
                        if resto==0:
                            print("\nVocê precisará encher o tanque {} vezes durante a sua rota".format(parte_inteira))
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(), combustivel_preco * vtanque*parte_inteira))
                            time.sleep(1)
                        if parte_inteira == 1:
                            print("\nVocê precisará encher o tanque {} vez e encher mais {:.2f} litros para completar o trajeto.".format(parte_inteira,comb2_exc))
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(), combustivel_preco *(vtanque *parte_inteira+comb2_exc)))
                            lin()
                            time.sleep(1)
                        if parte_inteira>1 and resto!=0:
                            print("\nVocê precisará encher o tanque {} vezes e encher mais {:.2f} litros para completar o trajeto.".format(parte_inteira, comb2_exc))
                            time.sleep(1)
                            print("O custo total com {}: R$ {:.2f}\n".format(combustivel.strip(),combustivel_preco * ((vtanque * parte_inteira) + comb2_exc)))
                            lin()
                        time.sleep(2)
            else:
                print(RED +"Você não digitou uma opção válida\n")

        except:
            print(RED +"Você não digitou uma opção válida\n")
            
    if variavel_central != '1' and variavel_central != '2':
        print(RED +"Você não digitou uma opção válida\n")
    time.sleep(1)
    cont= (input(RESET+'Deseja continuar planejando uma nova viagem? (s/n)   '))
    if cont == 's':
        system('cls')
        cont2 = 0
    elif cont == 'n':
        system('cls')
        cont2 = 1

    if cont != 's' and cont != 'n':
         print(RED +"Você não digitou uma opção válida\n")

time.sleep(0.5)
system('cls')
digitação(RESET + f'Até logo, {nome}!\nEspero vê-lo aqui em breve planejando uma nova viagem!\n')
print('''
--------------------------------------------
                SAINDO....
--------------------------------------------
      ''')
time.sleep(2)
system('cls')


