jogador = input('Escolha a classe (guerreiro, mago, arqueiro): ')
pontos_força = int(input('Digite os pontos de força ( de 1 a 20): '))
pontos_magia= int(input('Digite os pontos de magia (de 1 a 20): '))

result = ((jogador == 'mago' and pontos_força <= 10 and pontos_magia >=15 ) or (jogador == 'guerreiro' and pontos_força >= 15 and pontos_magia <= 10) or (jogador == 'arqueiro' and (pontos_força >= 5 and pontos_força <=15) and (pontos_magia >= 5 and pontos_magia <=15)))

print(f"Pontos de atributo consistentes com a classe escolhida: {result}")

