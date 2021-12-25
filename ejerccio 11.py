def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero


def capicua(numero):
    return numero == invertir_numero(numero)

numero= int(input("ingrese un numero: "))

for numero in numero:
    capicua = capicua(numero)
    print("El número es capicúa? {capicua}")