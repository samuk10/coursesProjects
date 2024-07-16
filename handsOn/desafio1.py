"""
sacar e depositar valor positivo e visualizar ambos no extrato na mesma variável
3x saques por dia no máximo R$ 500,00 por saque, total R$ 1500,00 por dia
if sem saldo suficiente, mostre uma mensagem de falta de saldo
extrato deve listar todos depositos e saques realizados na conta e no fim saldo atual.
os valores devem ser exibidos utilizando o formato R$ xxx.xx EX: R$ 100.00
"""

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_DIARIO_SAQUE = 1500
valor_saque_diario = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n================ EXTRATO ================")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")
            print("==========================================")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite_diario = valor_saque_diario + valor > LIMITE_DIARIO_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por saque.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif excedeu_limite_diario:
            print("Operação falhou! Limite diário de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            valor_saque_diario += valor
            print("\n================ EXTRATO ================")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print(f"Saques restantes: {LIMITE_SAQUES - numero_saques}")
            print("==========================================")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
