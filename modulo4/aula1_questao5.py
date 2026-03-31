n = int(input("Informe o número de respondentes: "))
soma = 0
i = 0
while (i < n):
    idade = int(input("Idade: "))
    soma = soma + idade
    i += 1

media = soma / n
print(media)
