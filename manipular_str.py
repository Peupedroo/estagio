string = "a b da  A asda"
encontrado = False
percorrer = 0
contagem = 0

while percorrer < len(string):
    if string[percorrer] == "a":
        contagem += 1
        print("A letra 'a' é minúscula")
    elif string[percorrer] == "A":
        contagem += 1
       
        print("A letra 'A' é maiúscula")
        break
    percorrer+=1    


print (contagem)
