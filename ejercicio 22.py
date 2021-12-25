#Construya un programa que dado un valor entero N, haga el cálculo de la función factorial utilizando estructuras iterativas. 

def factorial(numero):
        print( "Valor inicial) ->",numero
     if numero > 1:
        numero = numero * factorial(numero -1)
        print ("valor final )->",numero
    return numero