#Dado un (1) número, imprimir 0 si es par y 1 si es impar.
numero = 0
numero = int(input("Indique un número: "))
if (numero % 2) == 0:
    print(numero, " es par")
else:
  print(numero, " es impar")