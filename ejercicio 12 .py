numero=int(input("ingrese un numero:"))
centena=numero/100
decena=(numero%100)/10
unidad=(numero%100)%10

if(centena==unidad):
    print("el numero es capiuca")
else:
    print("el numero no es capiuca")        