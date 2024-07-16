def sacar(valor):
    """
    Function to perform a withdrawal operation based on the given value.
    Takes a single parameter 'valor' representing the withdrawal amount.
    No return value specified.
    """
    saldo = 1000

    if saldo >= valor:
        print("Saque realizado")
    else:
        print("Saldo insuficiente")
    print("Obrigado por utilizar nossos serviços")

def depositar(valor):
    """
    A function to deposit a given value into the account balance.
    Takes a single parameter 'valor' representing the amount to be deposited.
    No return value specified.
    """
    saldo = 500
    saldo += valor

sacar(1000)
