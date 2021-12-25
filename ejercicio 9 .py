#ESTRUCTURA DE CONTROLDE FLUJO DE DATOS.
#Todos los años que se dividen exactamente entre 400, o que son divisibles 
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
#Usando estas premisas crea un algoritmo que lea una fecha como un número 
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
#el mismo es un año bisiesto o no.

print('Determina si un año es bisiesto')
a=int(input("Introduce el año: "))
if a%4==0 and a%100!=0 or a%400==0:
    print(a," es un año bisiesto")
else:
  print(a," no es un año bisiesto")