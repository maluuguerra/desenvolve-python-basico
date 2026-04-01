import random 

x = random.randint (1, 10)

while True:
    y = int(input("Adivinhe um número de 1 a 10: "))

    if (y > x):
        print("Muito alto, tente novamente: ")
    elif (y < x):
        print("Muito baixo, tente novamente: ")
    else:
        print("Correto! o número é %d" %(x))
        break        