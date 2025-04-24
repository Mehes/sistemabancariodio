# Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    # Menu de Operações 
    print('    Banco Dio     ')
    print('[1] Depositar')
    print('[2] Sacar')
    print('[3] Extrato')
    print('[0] Sair')
    opcao = int(input('Digite a opção que deseja acessar: '))

    if opcao == 1:
        print('Depósito')
        deposito = int(input('Digite o valor que deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}'
            print(f'Você depositou R${deposito} reais.')
        else:
            print('Valor inválido para depósito.')

    elif opcao == 2:
        print('Saque')
        saque = int(input('Digite o valor que deseja sacar (limite de R$500 reais): '))
        if saque > saldo:
            print('Saldo insuficiente.')
        elif saque > limite:
            print('O valor excede o limite de saque por operação.')
        elif numero_saques >= limite_saques:
            print('Número máximo de saques excedido.')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}'
            numero_saques += 1
            print(f'O valor de R${saque} reais foi sacado.')
        else:
            print('Valor inválido para saque.')

    elif opcao == 3:
        print('Extrato')
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == 0:
        print('Você saiu!')
        break

    else:
        print('Opção inválida, tente novamente.')
