# proograma para verificar si un numero es positivo

# input
print("--------------------------------------")
print("----------numero positivo-------------")
print("--------------------------------------")
x = int(input("digite numero: "))

# processing 
if (x>0):
     rta = "positivo"
else:
     rta = "negativo"

# output 
print("---------------------------------------")
print("-------------resultado-----------------")
print("---------------------------------------")
print("el numero " + str(x) + " es " + rta)
