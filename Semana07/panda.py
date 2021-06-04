url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv'

import pandas as pd

# datos = pd.read_csv(url)
# print(datos)

# datos['tip']

# datos['smoker']

# Mostrar solo 4 columnas: 'total_bill', 'tip', 'smoker', 'time'

# columnas = ['total_bill','tip','smoker','time']
# datos[columnas]

# datos[['total_bill','tip','smoker','time']]

# Mostrar solo 2 columnas: 'total_bill' y 'day'

# columnas = ["total_bill", "day"]
# datos[columnas]

# datos[['total_bill', 'day']]

# Mostrar las 7 columnas y solo los primeros 5 registros

# datos.head(5)

# n_registros = 5
# datos2 = datos.head(n_registros)
# print(datos2)

# Mostrar las 3 columnas: 'tip', 'sex' y 'size' con solo los 10 primeros registros

# print(datos[['tip', 'sex', 'size']].head(10))

# n_registros = 10
# datos2 = datos.head(n_registros)[["tip","sex","size"]]
# print(datos2)

# datos[['tip', 'sex', 'size']].head(10)

# Valor booleanos (bits): 

# 1 es True
# 0 es False

# print(datos)

# datos['size']==3

# booleanos = (datos['size']==3)

# booleanos

# Mostrar todos los registros donde size=3

# print(datos[booleanos])

#  Mostrar todos los registros donde time='Dinner'

# din = (datos["time"]=="Dinner")
# print(datos[din])

# Mostrar todos los registros donde 'sex'='Female' y 'day'='Sun'

# booleanos = (datos['sex']=='Female') & (datos['day']=='Sun')
# print(booleanos)

# print(datos[booleanos])

# Mostrar todos los registros donde 'sex'='Male' y 'day'='Fri' y 'Smoker'='No'

# s=((datos['sex']=="Male") & (datos['day']=="Fri") & (datos['smoker']=="No"))
# print(datos[s])

# booleanos = (datos["sex"]=="Male") & (datos["day"]=="Fri") & (datos["smoker"]=="No")
# print(datos[booleanos])

# sds = (datos['sex'] == 'Male') & (datos['day'] == 'Fri') & (datos['smoker'] == 'No')
# datos[sds]

# Mostrar los registros donde el día es jueves o viernes: day='Fri' o day='Thur'

# sds = (datos['day'] == 'Fri') | (datos['day'] == 'Thur')
# datos[sds]

# states = ((datos["day"]=="Fri") | (datos["day"] == "Thur"))

# print(datos[states])

# s = ((datos["day"]) == "Fri") | ((datos["day"]) == "Thur")
# print(datos[s])

# filt = (datos['day'] == 'Fri') | (datos['day'] == 'Thur')
# print(datos[filt])

# Mostrar los priemros 8 registros donde 'sex'='Male' y 'day'='Fri' o 'day'='Thur' y 'Smoker'='Yes'

# male = (datos["sex"]=="Male")
# day = (datos["day"]=="Fri") | (datos["day"]=="Thur")
# smoker = (datos["smoker"]=="Yes")
# booleanos = male & day & smoker
# print(datos[booleanos].head(8))

# b = (datos['sex']=='Male') & ((datos['day']=='Fri') | (datos['day']=='Thur')) & (datos['smoker']=='Yes')
# print (datos[b].head(8))

# Mostrar la cantidad de personas que son fumadores

# fumadores = (datos['smoker'] == 'Yes')
# print(fumadores)

# conteos = fumadores.value_counts()
# print(conteos)

# print("La cantidad de fumadores es {}".format(conteos[1]))

# print("La cantidad de NO fumadores es {}".format(conteos[0]))

# Mostrar la cantidad de registros donde las personas son fumadoras y el día es domingo

# booleanos = (datos["smoker"]=="Yes") & (datos["day"]=="Sun")
# conteo = booleanos.value_counts()
# print(conteo)

# print("Hay {} registros donde las personas son fumadoras y el día es domingo".format(conteo[1]))

# Mostrar los primeros 10 registros donde sea cena y la propina sea mayor que 5.00

# booleanos = ((datos['tip']>5.00) & (datos['time']=='Dinner'))
# print(datos[booleanos].head(10))

# # Mostrar los registros donde size sea mayor que 5 y la factura total sea mayor que 45

# c = ((datos['size']>5) & (datos['total_bill']>45))
# print(datos[c])

# # Mostrar la cantidad de registros donde size sea mayor que 5 y la factura total sea mayor que 45

# booleanos = ((datos['size']>5) & (datos['total_bill']>45))
# conteos = booleanos.value_counts()
# print(conteos[1])

# print(booleanos.value_counts()[1])

# # Agrupar "sex" por sus valores

# print(datos.groupby('sex').size())

# print("Cantidad 'Female'={}".format(datos.groupby('sex').size()[0]))

# print("Cantidad 'Male'={}".format(datos.groupby('sex').size()[1]))

# # Agrupar 'day' y contar sus valores

# print(datos.groupby('day').size())

# # Agregación de columnas

# Crear una nueva columna llamada 'tip_rate' que contenga la división entre 'tip' y 'total_bill'

# datos.assign(tip_rate=datos['tip']/datos['total_bill'])

# # Considerar la columna 'tip' y 'day' donde se almacenen la media y el total respectivamente en un agrupamiento por día

# import numpy as np


# datos.groupby('day').agg({'tip':np.mean, 'day':np.size})

# np.mean([20,18,16])

# np.size([20,18,16])

# # La media de propinas los viernes

# datos2 = datos[datos['day']=='Fri']
# np.mean(datos2['tip'])

# # Hacer un resumen por 'smoker' y 'day' para mostrar el total de propinas y el promedio de propinas

# datos.groupby(['smoker','day']).agg({'tip':[np.size, np.mean]})

# # Resuir el promedio de propinas y total_bill por 'sex'

# datos.groupby('sex').agg({'tip':np.mean, 'total_bill':np.mean})

# # Programa


# def opcion1():
#   print("Bienvenido a la OPCION 1")
#   print("="*40)
#   N = int(input('Ingrese N: '))
#   print(datos.head(N))

# def opcion2():
#   print("Bienvenido a la OPCION 2")
#   print("="*40)
#   print(datos[['time', 'day','sex']])

# def menu():
#   opc = 1
#   while (opc!=3):
#     print("Bienvenido a nuestro Programa")
#     print("="*40)
#     print("[1] Mostrar los primeros N registros")
#     print("[2] Mostrar los registros con las columnas time, day y sex")
#     print("[3] Salir")
#     opc = int(input('Opción: '))
#     if opc == 1:
#       opcion1()  
#     elif opc==2:
#       opcion2()
        


# menu()

# # Días feriados

# Agregar una columna que se llame "feriado" y contenga la palabra "Feriado" si es sábado y domingo, pero contenga "Día de semana" si es cualquier otro día

# bool1 = datos['day']=='Sat'
# bool2 = datos['day']=='Sun'
# bool3 = bool1 | bool2

# print(bool3)

# M = len(bool3)
# feriados = []
# for i in range(M):
#   if bool3[i]==True:
#     feriados.append('Feriado')
#   else:  
#     feriados.append('Día de Semana')

# datos.assign(feriado=feriados)

