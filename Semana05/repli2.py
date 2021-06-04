
print("Ejercicio 2")
print("-"*40)
nombres = ["JUAN", "KARLA", "MANUEL", "FIORELLA"]
nombres_minus = []
for nom in nombres:
    nom = nom.lower()
    nombres_minus.append(nom)
print(nombres_minus)

#Programación declarativa
nombres_minus = [nom.lower() for nom in nombres]
print(nombres_minus)

print()