def arithmetic_arranger(problems, show_answers=False):
    # 1. Máximo de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        # 2. Operadores só podem ser + ou -
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Desenpacotamento da lista
        left, operator, right = parts

        # 3. Operandos só podem ser números
        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."

        # 4. Máximo de 4 dígitos
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Descobrir o tamanho de cada linha
        # Pega a linha maior e adiciona 2(ocupado pelo operador e espaço)
        width = max(len(left), len(right)) + 2

        # 5. Montagem das linhas
        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        dashes.append("-" * width)

        # 6. Se show_answers=True, calcula o resultado
        if show_answers:
            if operator == "+":
                result = str(int(left) + int(right))
            else:
                result = str(int(left) - int(right))
            answers.append(result.rjust(width))

    # Junta tudo com 4 espaços entre problemas
    arranged = (
        "    ".join(first_line)
        + "\n"
        + "    ".join(second_line)
        + "\n"
        + "    ".join(dashes)
    )
    if show_answers:
        arranged += "\n" + "    ".join(answers)
    return arranged


lista_1 = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49", "10 + 10"]
resultado = arithmetic_arranger(lista_1, True)
print(resultado)


"""
# O que retornará erro:
1. Só aceita 5 itens na lista, else error
2. Só aceita + e -, Se for * e / = error
3. Só aceitar digitos, else error
4. Cada operador pode ter 4 digitos, else error

# Formato do Output:
1. O Sinal deve estar na mesma linha do Segundo operando
2. Deve haver um único espaço entre o Sinal e o maior dos dois operandos
3. O Sinal fica sempre na posição [0](esquerda)
4. Números alinhados à direita
5. Deve haver 4 espaços por problema.
6. Deve ter Linhas no final de cada problema.
"""
