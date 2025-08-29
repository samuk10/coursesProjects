# 1. função normal
def quadrado(x):
    return x * x


print(quadrado(5))  # saída: 25

# 2. lambda function
quadrado = lambda x: x * x
print(quadrado(5))  # saída: 25

# 3. Map → aplica uma função a cada item de uma lista:
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]

# 4. Filter → filtra itens de uma lista:
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# 5. Sorted com chave:
nomes = ["Samuel", "Ana", "João", "Beatriz"]
ordenados = sorted(nomes, key=lambda nome: len(nome))
print(ordenados)  # ['Ana', 'João', 'Samuel', 'Beatriz']

# ? Exercício para você treinar
# 1. Crie um código em Python que:
# 2. Receba uma lista de números.
# 3. Use lambda + filter para pegar apenas os números maiores que 10.
# 4. Use lambda + map para elevar cada número ao quadrado.
# 5. Mostre o resultado final.

entrada = [5, 12, 7, 20, 3, 15]
maiores_que_dez = list(filter(lambda x: x > 10, entrada))
print(maiores_que_dez)
quadrados = list(map(lambda x: x * x, maiores_que_dez))
print(quadrados)  # saída esperada: [144, 400, 225]

# ? Novo exercício para você treinar
# Dada uma lista de palavras, faça:
# Use lambda + filter para pegar só as palavras que começam com a letra "a".
# Use lambda + map para transformar essas palavras em maiúsculas.
# Ordene o resultado em ordem alfabética usando sorted com lambda.

palavras = ["banana", "abacaxi", "uva", "ameixa", "laranja", "amora"]
contains_a = list(filter(lambda x: x[0] == "a", palavras))
contains_a_also = list(filter(lambda x: x.startswith("a"), palavras))
print(contains_a)  # ['abacaxi', 'ameixa', 'amora']
print(contains_a_also)  # ['abacaxi', 'ameixa', 'amora']
uppercase = list(map(lambda x: x.upper(), contains_a))
print(uppercase)  # ['ABACAXI', 'AMEIXA', 'AMORA']
