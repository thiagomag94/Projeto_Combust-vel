#Definição de funções

def lin():
    print("-"*75)

def lin2(msg):
    print("-"*75)
    print(msg)
    print("-"*75)


#PROGRAMA PRINCIPAL


lin2("CÁLCULO DE CUSTO DE COMBUSTÍVEL")
nome = input('Qual seu nome? ')
lin()
print('Olá, {}. Tudo bem? sou a assistente virtual dos FURICOS NO ASFALTO. \nTe ajudarei a planejar sua viagem..\nVamos lá?\n'.format(nome))
lin()

#seção de processamento interno dos dados obtidos
combustivel = input('Qual o combustível prefere utilizar? [Gasolina/Álcool/Eletricidade] ')

if combustivel == 'eletricidade' or combustivel=='ELETRICIDADE' or combustivel=='Eletricidade':

    print("Escolha dentre as opções de trajeto abaixo:\n")
    opcao = (input('1.Duas cidades [ida e volta]\n2.Rota calculada\n '))

    if opcao == 'Duas cidades' or opcao == '1':
        lin2('TRAJETO ENTRE DUAS CIDADES')

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
        lin()


        if distancia_iv==autonomia_elet:
            print('Você precisará carregar a bateria totalmente apenas uma vez')
        if distancia_iv < autonomia_elet:
            print('Você consumirá {}% de sua carga total para percorrer o trajeto completo (ida e volta) '.format(carga_consumida*100))
            print("Custo com energia elétrica: R$ {}".format(carga_preco*carga_consumida))
        if distancia_iv > autonomia_elet:
            if resto ==0:
                print('Você terá que recarregar {}x para completar o trajeto '.format(parte_inteira))
                print("Custo com energia elétrica: R$ {:.2f}".format(carga_preco * carga_consumida))
            if parte_inteira >=1 and resto!=0:
                print('Você terá que recarregar a bateria completamente {}x e mais {:.2f}% para completar o trajeto ida e volta '.format(parte_inteira,carga_restante))
                print("Custo com energia elétrica: R$ {:.2f}".format(carga_preco * (carga_consumida)))


        print('\nBoa viagem, {}!'.format(nome))
        lin()
        print("Espero te ver por aqui, planejando uma nova viagem, em breve!")

    elif opcao == "Rota calculada" or opcao == '2':
        lin2('ROTA COMPLETA PRÉ CALCULADA')

        autonomia_elet = float(input('Quantos Km/carga faz seu veículo elétrico? '))
        distancia = float(input('Qual o tamanho da rota em km ? '))
        carga_preco = float(input('Qual o preço médio por carga? '))
        vtanque = 1
        distancia_iv =  distancia
        carga_consumida = distancia_iv / autonomia_elet
        resto = (distancia_iv % autonomia_elet)
        parte_inteira = int(carga_consumida)
        carga_restante = resto * 100 / autonomia_elet
        parte_decimal = resto / autonomia_elet
        lin()

        if distancia_iv==autonomia_elet:
            print('Você precisará carregar a bateria totalmente apenas uma vez')
        if distancia_iv < autonomia_elet:
            print('Você consumirá {}% de sua carga total para percorrer o trajeto completo.'.format(carga_consumida*100))
            print("Custo com energia elétrica: R$ {:.2f}".format(carga_preco*carga_consumida))
        if distancia_iv > autonomia_elet:
            if resto ==0:
                print('Você terá que recarregar {}x para completar o trajeto '.format(parte_inteira))
                print("Custo com energia elétrica: R$ {:.2f}".format(carga_preco * carga_consumida))
            if parte_inteira >=1 and resto!=0:
                print('Você terá que recarregar a bateria completamente {}x e mais {:.2f}% para completar o trajeto ida e volta '.format(parte_inteira,carga_restante))
                print("Custo com energia elétrica: R$ {:.2f}".format(carga_preco * (carga_consumida)))


        print('\nBoa viagem, {}!'.format(nome))
        lin()
        print("Espero te ver por aqui, planejando uma nova viagem, em breve!")

else:

    #PARTE 2
    autonomia = float(input('Quantos Km/L faz seu veículo? '))
    distancia = float(input('Qual a distancia em Km entre as duas cidades? '))
    vtanque = float(input('Qual o volume total do tanque de combustível? '))
    combustivel_preco = float(input('Qual o preço médio por litro de combustível? '))
    print('')

    # distância que o veículo percorrerá até esvaziar o tanque
    dtc = autonomia * vtanque

    #quantidade de litros a abastecer por km rodado
    comb_abastecer = distancia/autonomia


    #quantidade excedente de combustível a ser utilizado na viagem de volta (para dtc>distancia)
    comb_exc = (dtc - distancia)/autonomia

#ida
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


    print('')
    print('Seu veículo faz {:.2f} Km com {:.2f} L de {} \n'.format(dtc, vtanque, combustivel))
    lin()

    # pergunta se quer calcular para ida e volta ou só ida
    condicao1 = input("Digite 1 para calcular o custo de ida ou 0 para ida e volta: ")
    lin()
    #ida
    if condicao1=='1':
        if distancia==dtc:
            print("Você precisará encher o tanque uma vez durante o trajeto de ida")
            print("O custo total com {}: R$ {:.2f}".format(combustivel,combustivel_preco*vtanque))
            lin()
        if distancia<dtc:
            print("Você precisará abastecer o tanque com {:.2f} litros ou encher o tanque uma vez durante o trajeto de ida\nCaso opte por encher o tanque, sobrarão {:.2f} litros para fazer {:.2f} km na viagem de volta.".format(comb_abastecer,comb_exc,(dtc-distancia)))
            lin()
            print("O custo total com {} sem encher o tanque: R$ {:.2f}".format(combustivel,comb_abastecer*combustivel_preco))
            print("O custo total caso deseje encher o tanque: R$ {:.2f}".format(vtanque*combustivel_preco))
            lin()
        if distancia>dtc:
            #divisão exata (enche o tanque mais de uma vez)
            if resto==0:
                print("\nVocê precisará encher o tanque {} vezes durante o trajeto de ida".format(parte_inteira))
                print("O custo total com {}: R$ {:.2f}".format(combustivel, combustivel_preco * vtanque*parte_inteira))
            if parte_inteira == 1:
                print("\nVocê precisará encher o tanque {} vez e encher mais {:.2f} litros para completar o trajeto de ida.".format(parte_inteira,comb2_exc))
                print("O custo total com {}: R$ {:.2f}".format(combustivel, combustivel_preco *(vtanque *parte_inteira+comb2_exc)))
                lin()
            if parte_inteira>1 and resto!=0:
                print("\nVocê precisará encher o tanque {} vezes e encher mais {:.2f} litros para completar o trajeto de ida.".format(parte_inteira, comb2_exc))
                print("O custo total com {}: R$ {:.2f}".format(combustivel,combustivel_preco * ((vtanque * parte_inteira) + comb2_exc)))
                lin()

    if condicao1=='0':

        if distancia_iv == dtc:
                print("Você precisará encher o tanque uma vez para completar o trajeto desejado")
                print("O custo total com {}: R$ {:.2f}".format(combustivel, combustivel_preco * vtanque))
                lin()
        if distancia_iv<dtc:
            print("Você precisará abastecer o tanque com {:.2f} litros ou encher o tanque uma vez durante o trajeto \nCaso opte por encher o tanque, sobrarão {:.2f} litros para fazer {:.2f} km em outra viagem.".format(comb_abastecer2,vtanque-comb_abastecer2,(dtc-distancia_iv)))
            lin()
            print("O custo total com {} sem encher o tanque: R$ {:.2f}".format(combustivel,comb_abastecer2*combustivel_preco))
            print("O custo total caso deseje encher o tanque: R$ {:.2f}".format(vtanque*combustivel_preco))
            lin()
        if distancia_iv>dtc:
            #divisão exata (enche o tanque mais de uma vez)
            if resto2==0:
                print("\nVocê precisará encher o tanque {} vezes para percorrer o trajeto desejado de {}km".format(parte_inteira2,distancia_iv))
                print("total de combustível gasto: {:.2f} litros".format(parte_inteira2*vtanque))
                print("O custo total com {}: R$ {:.2f}".format(combustivel, combustivel_preco * vtanque*parte_inteira2))
            if parte_inteira2 == 1:
                print("\nVocê precisará encher o tanque {} vez e encher mais {:.2f} litros para completar o trajeto desejado de {}km.".format(parte_inteira2,comb2_exc2,distancia_iv))
                print("Total de combustível gasto: {:.2f} litros".format(vtanque+comb2_exc2))
                print("O custo de ida e volta com {}: R$ {:.2f}".format(combustivel, combustivel_preco *(vtanque *parte_inteira2+comb2_exc2)))
                lin()
            if parte_inteira2>1 and resto2!=0:
                print("\nVocê precisará encher o tanque {} vezes e encher mais {:.2f} litros para completar o trajeto de {}km.".format(parte_inteira2, comb2_exc2,distancia_iv))
                print("Total de combustível gasto: {:.2f} litros".format(parte_inteira2*vtanque+comb2_exc2))
                print("O custo total com {}: R$ {:.2f}".format(combustivel,combustivel_preco * ((vtanque * parte_inteira2) + comb2_exc2)))
                lin()
    print('\nBoa viagem, {}!'.format(nome))
    lin()
    print("Espero te ver por aqui, planejando uma nova viagem, em breve!")
