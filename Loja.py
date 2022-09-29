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
totalcarrinho = 0
total_da_compra =0
total_compras = 0
total_mostrar_compras=  0 
compras_1 = 0
compras_2 = 0
compras_3 = 0
compras_4 = 0
compras_5 = 0
compras_6 = 0
compras_7 = 0
compras_8 = 0
compras_9 = 0

global selecao

# FUNÇÕES PARA MOSTRAR COMPRAS
def compras_produto():
    if selecao == 1:
        return compras_1
    elif selecao == 2:
        return compras_2
    elif selecao == 3:
        return compras_3
    elif selecao == 4:
        return compras_4
    elif selecao == 5:
        return compras_5
    elif selecao == 6:
        return compras_6
    elif selecao == 7:
        return compras_7
    elif selecao == 8:
        return compras_8
    elif selecao == 9:
        return compras_9
    
def valor_produto():
    if selecao == 1:
        return 112.00
    elif selecao == 2:
        return 95.00
    elif selecao == 3:
        return 49.90
    elif selecao == 4:
        return 169.00
    elif selecao == 5:
        return 120.00
    elif selecao == 6:
        return 135.00
    elif selecao == 7:
        return 12.99
    elif selecao == 8:
        return 183.00
    elif selecao == 9:
        return 219.90
    
def nome_produto():
    if selecao == 1:
        return "calça"
    elif selecao == 2:
        return "camisa"
    elif selecao == 3:
        return "bermuda"
    elif selecao == 4:
        return "saia"
    elif selecao == 5:
        return "blusa"
    elif selecao == 6:
        return "moletom"
    elif selecao == 7:
        return "meia"
    elif selecao == 8:
        return "tênis"
    elif selecao == 9:
        return "bota"
    
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

def exibir_menu_selecao():
    global qt_desejada,nome, selecao
    nome = str(input('\nInsira seu nome: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Bem vindo, {}!'.format(nome))
    selecao = 11
    while (selecao != 0):
        selecao = menu_itens()       
        if selecao != 0:
            qt_desejada = int(input('\nInsira a quantidade de itens desejados: '))
            registrar_item(selecao)
            # Valida se quantidade selecionada está disponível em estoque
            while (qt_desejada > qt and qt_desejada > 0):
                qt_desejada = int(input('\nEstoque insuficiente, a quantidade de itens disponíveis é {}.\nInsira a quantidade desejada ou insira 0 para cancelar: '.format(qt)))
                if qt_desejada >0:
                    continue
                else:
                    return 0
            registrar_venda()
            compras_feitas()
            atualizar_estoque(selecao)
                                
        else: 
            global totalcarrinho
            print('Valor total é de: R${}' .format(totalcarrinho))
            print('RETORNANDO...')
            totalcarrinho=0                                   
            input('\nDigite ENTER para Retornar\n')
            
def exibir_menu_repor():
    global qt, valor
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

def compras():
    if selecao == 1:
        return compras_1
    elif selecao == 2:
        return compras_2
    elif selecao == 3:
        return compras_3
    elif selecao == 4:
        return compras_4
    elif selecao == 5:
        return compras_5
    elif selecao == 6:
        return compras_6
    elif selecao == 7:
        return compras_7
    elif selecao == 8:
        return compras_8
    elif selecao == 9:
        return compras_9

def compras_feitas():
    global compras_1,compras_2,compras_3,compras_4,compras_5,compras_6,compras_7,compras_8,compras_9,qt_desejada
    if selecao == 1:
        compras_1 += qt_desejada
    elif selecao == 2:
        compras_2 += qt_desejada
        return compras_2
    elif selecao == 3:
        compras_3 += qt_desejada
        return compras_3
    elif selecao == 4:
        compras_4 += qt_desejada
        return compras_4
    elif selecao == 5:
        compras_5 += qt_desejada
        return compras_5
    elif selecao == 6:
        compras_6 += qt_desejada
        return compras_6
    elif selecao == 7:
        compras_7 += qt_desejada
        return compras_7
    elif selecao == 8:
        compras_8 += qt_desejada
        return compras_8
    elif selecao == 9:
        compras_9 += qt_desejada
        return compras_9   
# Registra a venda

def registrar_venda():
    os.system('cls' if os.name == 'nt' else 'clear')
    global qt,qt_desejada,total_da_compra, calca_qt, camisa_qt, bermuda_qt, saia_qt, blusa_qt, moletom_qt, meia_qt, tenis_qt, bota_qt, maior_comprador, cliente_maior_compra,nome, total_da_compra, valor_venda, totalcarrinho,total_mostrar_compras
    valor_venda = qt_desejada*valor
    confirmacao = input(
        '\nO valor total da venda foi R${:.2f}. Deseja confirmar? s/n: '.format(valor_venda)).lower()
    if confirmacao == 's':
        qt = qt - qt_desejada
        print('Venda registrada com sucesso!')
        print('O estoque agora é de {} unidades.'.format(qt))
        #Maior Compra
        total_da_compra = valor_venda
        totalcarrinho=total_da_compra+totalcarrinho
        total_mostrar_compras=total_da_compra+total_mostrar_compras
        if totalcarrinho > maior_comprador:
            maior_comprador = totalcarrinho
            cliente_maior_compra = nome
    elif confirmacao == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        return menu_itens
    else:
        print('Por favor, digite apenas s ou n')
        time.sleep(2.5)
        return registrar_venda()

            
    return qt, valor_venda

# Atualizar o Estoque

def atualizar_estoque(selecao):
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
    print('|  Calça          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(calca_qt).zfill(2), calca_valor, calca_qt*calca_valor, align='^', width='7'))
    print('|  Camisa         | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(camisa_qt).zfill(2), camisa_valor, camisa_qt*camisa_valor, align='^', width='7'))
    print('|  Bermuda        | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(bermuda_qt).zfill(2), bermuda_valor, bermuda_qt*bermuda_valor, align='^', width='7'))
    print('|  Saia           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(saia_qt).zfill(2), saia_valor, saia_qt*saia_valor, align='^', width='7'))
    print('|  Blusa          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(blusa_qt).zfill(2), blusa_valor, blusa_qt*blusa_valor, align='^', width='7'))
    print('|  Moletom        | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(moletom_qt).zfill(2), moletom_valor, moletom_qt*moletom_valor, align='^', width='7'))
    print('|  Meia           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(meia_qt).zfill(2), meia_valor, meia_qt*meia_valor, align='^', width='7'))
    print('|  Tênis          | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(tenis_qt).zfill(2), tenis_valor, tenis_qt*tenis_valor, align='^', width='7'))
    print('|  Bota           | {:{align}{width}} unidades     |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |'.format(str(bota_qt).zfill(2), bota_valor, bota_qt*bota_valor, align='^', width='7'))
    input('\nDigite ENTER para continuar\n')
    
#Mostrar Compras
def mostrar_compras():
    global total_mostrar_compras
    global selecao
    print("\n..:: MOSTRAR COMPRAS ::..\n")
    print('|     PRODUTO     |  QUANTIDADE COMPRADA  |  QUANTIDADE  ESTOQUE  |    VALOR UNITÁRIO    |   VALOR TOTAL   | TOTAL COMPRAS |')
    print('|  Calça          | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_1).zfill(2),str(calca_qt).zfill(2), calca_valor, calca_qt*calca_valor, align='^', width='7'))
    print('|  Camisa         | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_2).zfill(2),str(camisa_qt).zfill(2), camisa_valor, camisa_qt*camisa_valor, align='^', width='7'))
    print('|  Bermuda        | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_3).zfill(2),str(bermuda_qt).zfill(2), bermuda_valor, bermuda_qt*bermuda_valor, align='^', width='7'))
    print('|  Saia           | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_4).zfill(2),str(saia_qt).zfill(2), saia_valor, saia_qt*saia_valor, align='^', width='7'))
    print('|  Blusa          | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_5).zfill(2),str(blusa_qt).zfill(2), blusa_valor, blusa_qt*blusa_valor, align='^', width='7'))
    print('|  Moletom        | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_6).zfill(2),str(moletom_qt).zfill(2), moletom_valor, moletom_qt*moletom_valor, align='^', width='7'))
    print('|  Meia           | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_7).zfill(2),str(meia_qt).zfill(2), meia_valor, meia_qt*meia_valor, align='^', width='7'))
    print('|  Tênis          | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_8).zfill(2),str(tenis_qt).zfill(2), tenis_valor, tenis_qt*tenis_valor, align='^', width='7'))
    print('|  Bota           | {:{align}{width}} unidades      | {:{align}{width}} unidades      |  R${:{align}{width}.2f}           |   R${:{align}{width}.2f}     |###############|'.format(str(compras_9).zfill(2),str(bota_qt).zfill(2), bota_valor, bota_qt*bota_valor, align='^', width='7'))
    print('|  TOTAL COMPRAS  |########################################################################################|   R${:{align}{width}.2f}   |'.format(total_mostrar_compras, align='^', width='7'))                    
    input("\n\nPressione ENTER para continuar.")

#Mostrar Maior Compra
def maior_compra():
    global cliente_maior_compra, total_da_compra
    print('O Cliente que fez a maior compra foi o cliente {}' .format (cliente_maior_compra))
    print('Com o valor total da compra de R${:.2f}' .format (maior_comprador))
    input('\nDigite ENTER para retornar\n')
    #FALTA TABELA uma tabela com os itens comprados
    

# Loop de execução do programa
if __name__ == '__main__':
    escolha = 0

    while(escolha != 6):
        escolha = menu()

        if escolha == 1:  # Seleciona a função de registrar venda e solicita nome do usuário
            exibir_menu_selecao() # Exibe o menu de seleção do produto
                    
        elif escolha == 2: # Seleciona a função de repor o estoque
            selecao = 11

            while (selecao != 0):
                selecao = menu_itens()
                if selecao != 0:
                    qt, valor = registrar_item(selecao)
                    repor_estoque()
                    atualizar_estoque(selecao)
                    
                else:
                    print('RETORNANDO...')
                    input('\nDigite ENTER para continuar\n')
                    
        elif escolha == 3: # Seleciona a função de mostrar o estoque
            mostrar_estoque()
            
        elif escolha == 4: # Seleciona a função de mostrar compras
            mostrar_compras()
            
        elif escolha == 5: # Seleciona função de maior compra
            maior_compra()
            
        elif escolha == 6: # sai do programa
            print('SAINDO...')
            
        else:
            print('Opção inválida!')
            
            input('\nPressione ENTER para continuar')
