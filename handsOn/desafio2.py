"""
v1.0
sacar e depositar valor positivo e visualizar ambos no extrato na mesma variável
3x saques por dia no máximo R$ 500,00 por saque, total R$ 1500,00 por dia
if sem saldo suficiente, mostre uma mensagem de falta de saldo
extrato deve listar todos depositos e saques realizados na conta e no fim saldo atual.
os valores devem ser exibidos utilizando o formato R$ xxx.xx EX: R$ 100.00

v2.0
Criar funções para cadastrar usuário, cadastrar conta corrente(vincular com usuário) e listar contas
Substituir no loop sacar, depositar e extrato por funções

A função sacar deve receber os argumentos por keyword only.
- Sujestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
- Sujestão de retorno: saldo e extrato

A função depositar deve receber os argumentos por positional only.
- Sujestão de argumentos: saldo, valor, extrato.
- Sujestão de retorno: saldo e extrato

A função extrato deve receber os argumentos por positional only e keyword only.
- Sujestão de argumentos: saldo, valor, extrato.
- Sujestão de retorno: saldo e extrato

Devemos armazenar os usuários em uma lista, um usuário é composto por:
nome, data de nascimento, cpf e endereço.
Endereço é uma string com formato: logradouro, nro - bairro - Cidade/Sigla do Estado.
Deve ser armazenado somente os números do CPF. Não pode haver 2 users com mesmo CPF

Armazenar contas em uma lista, cada conta é composta por: agencia, número da conta e usuario.
O numero da conta é sequencial, iniciando em 1.
O numero da agencia é fixo: 0001.
O usuário pode ter mais de uma conta, mas uma conta pertence a somenta um usuário.
Para vincular um usuario a uma conta, filtre a lista de usuarios pelo CPF.

"""

def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (somente números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - Cidade/Sigla do Estado): ")

    # Verifica se já existe um usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário com esse CPF.")
            return
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")


def cadastrar_conta_corrente(usuarios, contas, numero_conta):
    cpf = input("Informe o CPF do usuário: ")

    # Procura pelo usuário com o CPF informado
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado.")
        return

    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    })

    print("Conta corrente cadastrada com sucesso!")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {usuario['nome']}, CPF: {usuario['cpf']}")


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite por saque.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    # Inicialização das listas e variáveis
    usuarios = []
    contas = []
    numero_conta = 1

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu_principal = """
    [1] Cadastrar usuário
    [2] Cadastrar conta corrente
    [3] Listar contas
    [4] Acessar conta
    [5] Sair
    => """

    menu_conta = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """



    while True:
        opcao_principal = input(menu_principal)

        if opcao_principal == "1":
            cadastrar_usuario(usuarios)
        elif opcao_principal == "2":
            cadastrar_conta_corrente(usuarios, contas, numero_conta)
            numero_conta += 1
        elif opcao_principal == "3":
            listar_contas(contas)
        elif opcao_principal == "4":
            cpf = input("Informe o CPF do usuário para acessar a conta: ")

            conta_usuario = None
            for conta in contas:
                if conta["usuario"]["cpf"] == cpf:
                    conta_usuario = conta
                    break

            if not conta_usuario:
                print("Conta não encontrada para o CPF informado.")
                continue

            while True:
                opcao_conta = input(menu_conta)

                if opcao_conta == "d":
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)
                    exibir_extrato(saldo, extrato=extrato)
                    print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")

                elif opcao_conta == "s":
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato, numero_saques = sacar(
                        saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                        numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
                    )
                    exibir_extrato(saldo, extrato=extrato)
                    print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")

                elif opcao_conta == "e":
                    exibir_extrato(saldo, extrato=extrato)

                elif opcao_conta == "q":
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")
        elif opcao_principal == "5":
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")
main()
