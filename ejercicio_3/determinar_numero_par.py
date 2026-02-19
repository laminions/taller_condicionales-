# programa paea verificar si un numero es par

# input
print("-------------------------------------------")
print("--------------numero par/impar-------------")
print("-------------------------------------------")
x = int(input("digite numero: "))

# processing 
mod = x%2
if(mod == 0):
    rta = "PAR"
else:
    rta = "IMPAR"

# output
print("--------------------------------------------")
print("---------------resultado--------------------")
print("--------------------------------------------")
print("el numero " + str(x) + " es " + rta) 
