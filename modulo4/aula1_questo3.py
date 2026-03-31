while True:
    n1 = int(input("Valor de n1: "))
    n2 = int(input("Valor de n2: "))
    n3 = int(input("Valor de n3: "))

    media = (n1 + n2 + n3) / 3

    if(media >= 60):
        print("Aprovado ")
        break
    elif(media >= 40):
        print("Recuperação ")
        break
    elif(media < 40):
        print("Reprovado ")
        break
print("fim")




