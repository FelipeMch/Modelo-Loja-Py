import os
import time

# Estoque e preços
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

#Variavel 
maior_comprador = 0
cliente_maior_compra = ''
selecao_atual =0

# Menu de seleção de função
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
# Menu de seleção de produtos


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
    if item < 0 or item > 9:
        print('!!! NÚMERO INVÁLIDO !!! \n\n###### DIGITE NUMEROS QUE ESTÃO NO MENU ######')
        time.sleep(3.5)
        return menu_itens()
    return item

# Armazena o input do usuário nas variáveis principais de quantidade e valor


def registrar_item(item):
    global qt, valor
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

# Registra a venda


def registrar_venda():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt, valor, calca_qt, camisa_qt, bermuda_qt, saia_qt, blusa_qt, moletom_qt, meia_qt, tenis_qt, bota_qt, maior_comprador, cliente_maior_compra,nome, total_da_compra
    valor_venda = qt_desejada*valor
    confirmacao = input(
        '\nO valor total da venda foi R${:.2f}. Deseja confirmar? s/n: '.format(valor_venda)).lower()
    if confirmacao == 's':
        qt = qt - qt_desejada
        print('Venda registrada com sucesso!')
        print('O estoque agora é de {} unidades.'.format(qt))
        #Maior Compra
        total_da_compra = valor_venda
        if total_da_compra > maior_comprador:
            maior_comprador = total_da_compra
            cliente_maior_compra = nome
    elif confirmacao == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        return menu_itens
    else:
        print('Por favor, digite apenas s ou n')
        time.sleep(2.5)
        return registrar_venda()
            
    return qt, valor_venda

def atualizar_estoque():
    global calca_qt, camisa_qt, bermuda_qt, saia_qt, blusa_qt, moletom_qt, meia_qt, tenis_qt, bota_qt
    if selecao == 1:
        calca_qt = qt
    elif selecao == 2:
        camisa_qt = qt
    elif selecao == 3:
        bermuda_qt = qt
    elif selecao == 4:
        saia_qt = qt
    elif selecao == 5:
        blusa_qt = qt
    elif selecao == 6:
        moletom_qt = qt
    elif selecao == 7:
        meia_qt = qt
    elif selecao == 8:
        tenis_qt = qt
    elif selecao == 9:
        bota_qt = qt
    return calca_qt, camisa_qt, bermuda_qt, saia_qt, blusa_qt, moletom_qt, meia_qt, tenis_qt, bota_qt

# Repõe o estoque


def repor_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt
    qt_repor = int(input('Quantas unidades deseja repor? :'))
    qt = qt + qt_repor
    print('O estoque agora é de {} unidades.'.format(qt))
    return qt


# Mostra o estoque atual
def mostrar_estoque():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt, valor
    print('\n..:: ESTOQUE ::..\n')
    print('|     PRODUTO     |      QUANTIDADE      |    VALOR UNITÁRIO    |   VALOR TOTAL   |')
    print('|  Calça          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        calca_qt, calca_valor, calca_qt*calca_valor, align='^', width='7'))
    print('|  Camisa         | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        camisa_qt, camisa_valor, camisa_qt*camisa_valor, align='^', width='7'))
    print('|  Bermuda        | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        bermuda_qt, bermuda_valor, bermuda_qt*bermuda_valor, align='^', width='7'))
    print('|  Saia           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        saia_qt, saia_valor, saia_qt*saia_valor, align='^', width='7'))
    print('|  Blusa          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        blusa_qt, blusa_valor, blusa_qt*blusa_valor, align='^', width='7'))
    print('|  Moletom        | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        moletom_qt, moletom_valor, moletom_qt*moletom_valor, align='^', width='7'))
    print('|  Meia           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        meia_qt, meia_valor, meia_qt*meia_valor, align='^', width='7'))
    print('|  Tênis          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        tenis_qt, tenis_valor, tenis_qt*tenis_valor, align='^', width='7'))
    print('|  Bota           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(        bota_qt, bota_valor, bota_qt*bota_valor, align='^', width='7'))
    
def mostrar_compras():
    print('print')
    
def maior_compra():
    global cliente_maior_compra, total_da_compra
    print('O Cliente que fez a maior compra foi o cliente {}' .format (cliente_maior_compra))
    print('Com o valor total da compra de R${:.2f}' .format (maior_comprador))
    #FALTA TABELA uma tabela com os itens comprados
    



# Loop de execução do programa
if __name__ == '__main__':
    escolha = '0'

    while(escolha != 6):
        escolha = menu()

        if escolha == 1:  # Seleciona a função de registrar venda e solicita nome do usuário
            nome = str(input('\nInsira seu nome: '))
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Bem vindo, {}!'.format(nome))

            # Exibe o menu de seleção do produto
            selecao = 11
            while (selecao != 0):
                selecao = menu_itens()
                if selecao != 0:
                    qt_desejada = int(input('\nInsira a quantidade de itens desejados: '))
                    qt, valor = registrar_item(selecao)
                    # Valida se quantidade selecionada está disponível em estoque
                    while (qt_desejada > qt and qt_desejada > 0):
                        qt_desejada = int(input(
                            '\nEstoque insuficiente, a quantidade de itens disponíveis é {}.\nInsira a quantidade desejada ou insira 0 para cancelar: '.format(qt)))
                    registrar_venda()
                    atualizar_estoque()
                    
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
        elif escolha == 4:
            mostrar_compras()
            input('\nPressione ENTER para continuar')
        elif escolha == 5:
            maior_compra()
            input('\nPressione ENTER para continuar')
        elif escolha == 6:
            print('SAINDO...')
        else:
            print('Opção inválida!')
