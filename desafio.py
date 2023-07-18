def menu():
    menu = '''\t *** MENU ***
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair

Selecione a opção desejada: '''
    return int(input(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Operação inválida! Valor informado não é válido.\n')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print('Operação inválida! Saldo insuficiente.\n')
    elif limite_excedido:
        print('Operação inválida! Valor do saque excede o limite.\n')
    elif saques_excedido:
        print('Operação inválida! Você já realizou o número máximo de saques permitido.\n')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Realizado saque no valor de R$ {valor:.2f}')
    else:
        print('Operação inválida! Valor informado não é válido.\n')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('______ EXTRATO ______')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('_____________________\n')


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF [apenas números]: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print('Usuário não encontrado.')


def listar_contas(contas):
    for conta in contas:
        contas_listadas = f'''\tAgência: {conta['agencia']}
    C/C: {conta['numero_conta']}
    Titular: {conta['usuario']['nome']}
'''
        print('_____________________')
        print(contas_listadas)


def criar_usuario(usuarios):
    cpf = input('Informe o CPF [apenas números]: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('CPF já cadastrado.')
        return

    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento [dd/mm/aaaa]: ')
    endereco = input('Endereço [logradouro, nº - bairro - cidade/sigla estado]: ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1:
            valor = float(input('Informe o valor do depósito: R$ '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Informe o valor do saque: R$ '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print('Opção inválida!\n')


main()


