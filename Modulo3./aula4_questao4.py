distancia = int(input('Distancia em km: '))
peso = int(input('Peso em kg: '))
valor = 0
if(peso > 10):
    valor += 10
else:
    valor = 0    

if(distancia <= 100):
    valor = peso * 1
if(distancia >= 101 and distancia <= 300):
    valor = peso * 1.50    
if(distancia > 300):
    valor = peso * 2

print(valor)