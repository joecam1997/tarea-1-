#El IMC resulta de la división de la masa del individuo (en kilogramos) entre el 
#cuadrado de la estatura (en metros). El índice de masa corporal es un indicador 
#del peso de una persona en relación con su altura.
#Clasificación del IMC de acuerdo con la OMS de la ONU:
#a. Menor a 16: Criterio de ingreso.
#b. 16 a 16.9: infra peso.
#c. 17 a 18.4: bajo peso.
#d. 18.5 a 24.9: peso normal.
#e. 25 a 29.9: sobrepeso.
#f. 30 a 34.9: obesidad pre-mórbida.
#g. 40 a 45: obesidad mórbida.
#h. Mayor a 45: obesidad híper-mórbida.


masa = float(input('Inserte su masa en kilogramos:'))
estatura = float(input('Inserte su estatura en metros:'))

imc = masa / estatura**2

if imc < 16:
    print('Tiene delgadez severa')
elif imc >=16 and imc < 17 :
    print('Tiene delgadez moderada')
elif imc >=17 and imc < 18.5 :
    print('Tiene delgadez leve')
elif imc >=18.5 and imc < 25 :
    print('Tiene IMC normal')
elif imc >=25 and imc < 30 :
    print('Tiene preobesidad')
elif imc >=30 and imc < 35 :
    print('Tiene obesidad leve')
elif imc >=35 and imc < 40 :
    print('Tiene obesidad media')
elif imc >= 40 :
    print('Tiene obesoidad morbida')
else:
    print('Opcion invalida')

    print('Su imc fue de ', imc)