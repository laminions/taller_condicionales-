# programa calcular costo de una llamada

# input
print("--------------------------------")
print("--------costo llamada-----------")
print("--------------------------------")
min = int(input("digite la duracion de la llamada de minutos: "))

# processing 
if (min <= 3):
    costo_llamada = 500
else: 
    costo_llamada = 500 + (min - 3)*100

# output
print("--------------------------------------")
print("-------------resultado----------------")
print("--------------------------------------")
print("duracion de la llamada: " + str(Min))
print("costo de la llamada: " + str(costo_llamada))
