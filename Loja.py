import os

qtd_calca = 0
qtdCamisa = 0
#--------------------------MENU---------------------------------
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Loja ::.. \n')
    print('1- Registrar venda')
    print('2- Repor estoque')
    print('3- Mostrar estoque')
    print('4- Mostrar compras')
    print('5- Maior compra')
    print('6- Sair')
    item = input('\nEscolha uma opção: ')
    return item
#-------------------------ITENS---------------------------------
def calca():
    codigo = 1
    desc = 'Calça'
    global estoque
    estoque = 20 + qtd_calca
    valor = 112.00
    print(codigo,'     ', desc,'    ', estoque,'     ', valor)

def camisa():
    codigo = 2
    desc = 'Camisa'
    global estoque
    estoque = 18 + qtdCamisa
    valor = 95.00
    print(codigo,'     ', desc,'   ', estoque,'     ', valor)
#---------------------PRINCIPAL--------------------------------
def opcao_1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Registrar venda ::..')

def opcao_2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Repor estoque ::..')
    cod = input('\nInforme o código do produto: ')
    global qtd_calca
    global qtdCamisa

    if cod == '1':
        qtd_calca = int(input('\nDigite a quantidade que irá repor: '))
    
    elif cod == '2':
        qtdCamisa = int(input('\nDigite a quantidade que irá repor: '))
        
       

def opcao_3():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Mostrar estoque ::..')
    print('\ncódigo, descrição, estoque, valor')
    calca()
    camisa()

def opcao_4():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Mostrar compras ::..')

def opcao_5():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Maior compra ::..')

def opcao_6():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n opção 6')
#------------------------OPÇÕES DO MENU-----------------------
escolha = '0'

while(escolha != 6):
    escolha = menu()
    if escolha == '1':
        opcao_1()
    elif escolha == '2':
        opcao_2()
    elif escolha == '3':
        opcao_3()
    elif escolha == '4':
        opcao_4()
    elif escolha == '5':
        opcao_5()
    elif escolha == '6':
        print('\n Saindo...\n')
    else:
        print('\n Opção inválida!\n')
    input('\nPressione ENTER para continuar')
#-------------------------FIM--------------------------------
#teste