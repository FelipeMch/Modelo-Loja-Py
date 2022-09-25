import os

#Estoque e preços
calca_valor = float(112.00)
calca_qt = int(20)
camisa_valor = float(95.00)
camisa_qt = int(18)
bermuda_valor = float(49.90)
bermuda_qt = int(23)
saia_valor = float(169.00)
saia_qt = int(12)
blusa_valor = float(120.00)
blusa_qt = int(9)
moletom_valor = float(135.00)
moletom_qt = int(4)
meia_valor = float(12.99)
meia_qt = int(17)
tenis_valor = float(183.00)
tenis_qt = int(8)
bota_valor = float(219.90)
bota_qt = int(3)


#Menu de seleção de função
def menu():
  os.system('cls' if os.name == 'nt' else 'clear') 
  print('\n..:: PONTO DE VENDA ::..\n')
  print('1 - Registrar venda')
  print('2 - Repor estoque')
  print('3 - Mostrar estoque')
  print('4 - Mostrar compras')
  print('5 - Maior compra')
  print('6 - Sair')
  opcao = int(input('Escolha uma opção: '))
  return opcao
#Menu de seleção de produtos

def menu_itens():
    print('\n..:: PRODUTOS ::..\n')
    print('1 - Calça')
    print('2 - Camisa')
    print('3 - Bermuda')
    print('4 - Saia')
    print('5 - Blusa')
    print('6 - Moletom')
    print('7 - Meia')
    print('8 - Tênis')
    print('9 - Bota')
    print('0 - Retornar')
    item = int(input('\nInsira o item desejado: '))
    return item

#Armazena o input do usuário nas variáveis principais de quantidade e valor
def registrar_item(item):
    if item == 1:
        qt = calca_qt
        valor = calca_valor
    elif item == 2:
        qt = camisa_qt
        valor = camisa_valor
    elif item == 3:
        qt = bermuda_qt
        valor = bermuda_valor
    elif item == 4:
        qt = saia_qt
        valor = saia_valor
    elif item == 5:
        qt = blusa_qt
        valor = blusa_valor
    elif item == 6:
        qt = moletom_qt
        valor = moletom_valor
    elif item == 7:
        qt = meia_qt
        valor = meia_valor
    elif item == 8:
        qt = tenis_qt
        valor = tenis_valor
    elif item == 9:
        qt = bota_qt
        valor = bota_valor
    return qt, valor
    
def registrar_venda():
    os.system('cls' if os.name == 'nt' else 'clear')
    valor_venda = qt_desejada*valor
    confirmacao = input('\nO valor total da venda foi R${:.2f}. Deseja confirmar? s/n: '.format(valor_venda)).lower()
    return confirmacao

#Loop de execução do programa
if __name__ == '__main__':
    escolha = '0'

    while(escolha != 6):
        escolha = menu()

        if escolha == 1: #Seleciona a função de registrar venda e solicita nome do usuário
                nome = str(input('\nInsira seu nome: '))
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Bem vindo, {}!'.format(nome))
                
                #Exibe o menu de seleção do produto
                selecao = 11
                while (selecao != 0):
                    selecao = menu_itens()
                    if selecao != 0:    
                        qt, valor = registrar_item(selecao)
                        qt_desejada = int(input('\nInsira a quantidade de itens desejados: '))

                        #Valida se quantidade selecionada está disponível em estoque
                        while (qt_desejada > qt):
                            while (qt_desejada > 0):
                                qt_desejada = int(input('\nEstoque insuficiente, a quantidade de itens disponíveis é {}.\nInsira a quantidade desejada ou insira 0 para cancelar: '.format(qt)))
                        registrar_venda()        
                    else:
                        print('RETORNANDO...')            
                        input('\nDigite ENTER para continuar\n')            
        elif escolha == 6:
            print('SAINDO...')
        else:
            print('Opção inválida!') 