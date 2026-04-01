import random
import math

soma = 0
n = int(input('Informe o número valores: '))

for i in range(n):
    x = random.randint(1,100)
    print(x)
    soma = soma + x


result = math.sqrt(soma)

print(soma)
