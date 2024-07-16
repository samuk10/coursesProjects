MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Qual sua idade? "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Menor de idade, ainda não pode tirar a CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")
