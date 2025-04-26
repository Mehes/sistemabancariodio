# Menu Principal
def menu_principal():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    limite_saques = 3
    usuarios = []

    while True:
        print('    Banco Dio     ')
        print('[1] Depositar')
        print('[2] Sacar')
        print('[3] Extrato')
        print('[4] Cadastro de Usuário')
        print('[5] Cadastro de Conta ')
        print('[0] Sair')
        opcao = int(input('Digite a opção que deseja acessar: '))

        if opcao == 1:
            print('Depósito')
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 2:
            print('Saque')
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, limite_saques)
        elif opcao == 3:
            print('Extrato')
            verificar_extrato(saldo, extrato)
        elif opcao == 4:
            print('Cadastrar Usuário')
            cadastar_usuario(usuarios)
        elif opcao == 5:
            print('Cadastrar Conta')
            cadastrar_conta(usuarios)
        elif opcao == 0:
            print('Você saiu!')
            break
        else:
            print('Opção inválida, tente novamente.')

def depositar(saldo, extrato):
    deposito = int(input('Digite o valor que deseja depositar: '))
    if deposito > 0:
        saldo += deposito
        extrato.append(f'Depósito: R${deposito:.2f}')
        print(f'Você depositou R${deposito:.2f} reais.')
    else:
        print('Valor inválido para depósito.')
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    saque = int(input('Digite o valor que deseja sacar (limite de R$500 reais): '))
    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque > limite:
        print('O valor excede o limite de saque por operação.')
    elif numero_saques >= limite_saques:
        print('Número máximo de saques excedido.')
    elif saque > 0:
        saldo -= saque
        extrato.append(f'Saque: R${saque:.2f}')
        numero_saques += 1
        print(f'O valor de R${saque:.2f} reais foi sacado.')
    else:
        print('Valor inválido para saque.')
    return saldo, extrato, numero_saques

def verificar_extrato(saldo, extrato):
    print('\n===== EXTRATO =====')
    if not extrato:
        print('Nenhuma movimentação realizada.')
    else:
        for operacao in extrato:
            print(operacao)
    print(f'\nSaldo atual: R${saldo:.2f}')
    print('===================')

def cadastar_usuario(usuarios):
    nome = input('Digite o nome a ser cadastrado: ')
    data_nasc = input('Digite a sua data de nascimento: (DD/MM/AAAA) ')
    cpf = input('Digite o CPF: (Somente números, sem caracteres)')
    while not validar_cpf(cpf):
        print("CPF inválido! Deve conter exatamente 11 números.")
        cpf = input("Digite o CPF (somente números): ")
    endereco = input('Digite o seu endereço: (Rua, Número e Bairro) ')
    usuario = {
        "nome": nome,
        "data de nascimento": data_nasc,
        "cpf": cpf,
        "endereço": endereco
    }
    usuarios.append(usuario)
    print('\n Usuário cadastrado com sucesso!')
    return usuario

contas = []  # Lista para armazenar as contas criadas

def cadastrar_conta(usuarios):
    cpf = input("\nDigite seu CPF para verificar se está cadastrado: ")
    
    # Verificar se o CPF está no cadastro de usuários
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break
    
    if usuario is None:
        print("Usuário não encontrado! Cadastre-se primeiro.")
        return
    
    # Gerar o número da conta (só precisa encontrar o próximo número disponível)
    numero_conta = len(contas) + 1  # O número de conta começa em 1 e vai subindo
    
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    
    contas.append(conta)
    
    print(f"\nConta criada com sucesso!")
    print(f"Agência: 0001 | Número da Conta: {numero_conta} | CPF: {cpf}")



def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


    

# Executar
menu_principal()
