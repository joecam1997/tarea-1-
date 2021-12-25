#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit 
#de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))