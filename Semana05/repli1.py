print("Ejercicio 1")
print("-"*40)
numeros = [1, 3, 5, 10]
#Programación Imperativa
suma = 0
for i in numeros:
    suma += i*2
print(suma)

#Programación declarativa
suma = sum([x*2 for x in numeros])
print(suma)
print()



