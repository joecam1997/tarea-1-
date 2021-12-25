#Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades, 
#decenas, centenas y unidades de mil.
print(" MOSTRAR LA UNIDAD,DECENA CENTENA,UNIDAD DE MIL")
num = int(input("Ingrese Un Número de 4 Cifras : "))
unimil=(num-(num%100))/100
cen = (num-(num%100))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
print("Centena : ",int (cen))
print("Decena : ",int (dec))
print("Unidad : ",int (uni))
print("unidad de mil :",int(unimil))
