sexo = input('Informe o seu sexo: ')
idade = int(input('Informe sua idade: '))
trabalho = int(input("Informe os anos trabalhados: "))

aposentadoria = ((sexo == 'f' and idade >= 60) or (sexo == 'm' and idade >= 65) or (trabalho >= 30) or (idade >= 60 and trabalho >= 25))

print(f"Possibilidade de aposentadoria: {aposentadoria}")