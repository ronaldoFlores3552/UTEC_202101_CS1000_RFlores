print()
print("Ejercicio 4")
print("-"*40)
numeros = [1,2,3,4,5]
pares = []
for i in numeros:
    if i%2 == 0:
        pares.append(i)
print(pares)

#Programación declarativa
pares = [i for i in numeros if i%2==0]
print(pares)
  