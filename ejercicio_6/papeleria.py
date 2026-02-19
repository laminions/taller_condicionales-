# inicio
print("..........")
print("bienvenido")
print("..........")

print("-------------------------------")
p= int(input("ingrese el valor de el producto "))
print("------------------------------------")

# proceso

if p <= 3000:
    ganancia=p*0.25
else:
    if p > 6000:
        ganancia= p*0.25
    else:
        ganancia= 500

    #precio final
    
    p_c=p+ganancia

# output
print("...................................")
print("la ganancia es: " +str(ganancia))
print("...................................")

print("...................................")
print("el precio final es " +str(p_c))
print("...................................")


