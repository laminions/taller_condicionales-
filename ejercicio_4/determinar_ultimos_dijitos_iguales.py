# programa para verificar si los dos ultimos digitos de un numero son iguales 

# input
print("---------------------------------------------")
print("------ultimos digitos iguales----------------")
print("---------------------------------------------")
x = int(input("digite un numero: "))

# processing 
ultimo_digito = % 10
penultimo_digito = (x//10)%10
if (ultimo_digito == penultimo_digito):
    rta = "IGUALES"
else:
    rta = "DIFERENTES"

# output 
print("-------------------------------------")
print("-------------resultado---------------")
print("--------------------------------------")
print("El numero ingreso fue: " + str(x))
print("su ultimo digitoes: " + str(ultimo_digito))
print("su penultimodigito es: + str(penultimo_digito)")
print("los dos ultimos digitos son " + rta)
