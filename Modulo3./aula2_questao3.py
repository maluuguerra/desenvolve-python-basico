idade = int(input('Digite sua idade: '))
jogos = input('Ja jogou pelo menos 3 jogos de tabuleiro? ')
vencidos = int(input('Quantos jogos ja venceu? '))

result = ((idade >= 16 and idade <= 18) and (jogos == 'True') and (vencidos >= 1))
print(f'Apto para ingressar no clube de jogos de tabuleiro: {result} ')
