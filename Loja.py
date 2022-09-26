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
    global qt, valor
    if item == 1:
        qt = 20
        valor = 112.00
    elif item == 2:
        qt = 18
        valor = 95.00
    elif item == 3:
        qt = 23
        valor = 49.90
    elif item == 4:
        qt = 12
        valor = 169.00
    elif item == 5:
        qt = 9
        valor = 120.00
    elif item == 6:
        qt = 4
        valor = 135.00
    elif item == 7:
        qt = 17
        valor = 12.99
    elif item == 8:
        qt = 8
        valor = 183.00
    elif item == 9:
        qt = 3
        valor = 219.90
    return qt, valor

#Registra a venda    
def registrar_venda():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt, valor
    valor_venda = qt_desejada*valor
    confirmacao = input('\nO valor total da venda foi R${:.2f}. Deseja confirmar? s/n: '.format(valor_venda)).lower()
    if confirmacao == 's':
        qt = qt - qt_desejada
        print('Venda registrada com sucesso!')
        print('O estoque agora é de {} unidades.'.format(qt))
    return qt, valor_venda

#Repõe o estoque
def repor_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt
    qt_repor = int(input('Quantas unidades deseja repor? :'))
    qt = qt + qt_repor
    print('O estoque agora é de {} unidades.'.format(qt))
    return qt


#Mostra o estoque atual
def mostrar_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt, valor
    print('\n..:: ESTOQUE ::..\n')
    print('PRODUTO   |   QUANTIDADE  |   VALOR UNITÁRIO |   VALOR TOTAL')
    print('Calça     | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(calca_qt, calca_valor, calca_qt*calca_valor))
    print('Camisa    | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(camisa_qt, camisa_valor, camisa_qt*camisa_valor))
    print('Bermuda   | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(bermuda_qt, bermuda_valor, bermuda_qt*bermuda_valor))
    print('Saia      | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(saia_qt, saia_valor, saia_qt*saia_valor))
    print('Blusa     | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(blusa_qt, blusa_valor, blusa_qt*blusa_valor))
    print('Moletom   | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(moletom_qt, moletom_valor, moletom_qt*moletom_valor))
    print('Meia      | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(meia_qt, meia_valor, meia_qt*meia_valor))
    print('Tênis     | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(tenis_qt, tenis_valor, tenis_qt*tenis_valor))
    print('Bota      | {} unidades   |  R${:.2f}        |   R${:.2f}'.format(bota_qt, bota_valor, bota_qt*bota_valor))
    input('\nPressione ENTER para continuar')

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
                        qt_desejada = int(input('\nInsira a quantidade de itens desejados: '))
                        qt, valor = registrar_item(selecao)
                        #Valida se quantidade selecionada está disponível em estoque
                        while (qt_desejada > qt and qt_desejada > 0):                           
                            qt_desejada = int(input('\nEstoque insuficiente, a quantidade de itens disponíveis é {}.\nInsira a quantidade desejada ou insira 0 para cancelar: '.format(qt)))
                        registrar_venda()        
                    else:
                        print('RETORNANDO...')            
                        input('\nDigite ENTER para continuar\n')            
        elif escolha == 2:
            selecao = 11

            os.system('cls' if os.name == 'nt' else 'clear')
            while (selecao != 0):
                selecao = menu_itens()
                if selecao != 0:
                    qt, valor = registrar_venda(selecao)
                    repor_estoque()
                else:
                    print('RETORNANDO...')
                    input('\nDigite ENTER para continuar\n')
        elif escolha == 3:
            mostrar_estoque()
            input('\nPressione ENTER para continuar')
        elif escolha == 6:
            print('SAINDO...')
        else:
            print('Opção inválida!') 