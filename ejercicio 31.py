
#Construya un programa que dado un valor entero N, haga el cálculo de la función factorial utilizando estructuras iterativas.        
  def ejercicio4(self):  
      numero=int(input("ingrese numero: "))
      factorial=1
      if numero!=0:
        for i in range(1,numero+1):
         factorial=factorial*i
      print("El factorial:",factorial)  

# Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
# peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
# base en dicha secuencia se desea realizar un estudio a fin de conocer    
  def ejercicio7(self):
        edad=[20,18,32,19,22,40]
        peso=[42,52,49,47,50,46]
        estatura=[1.45,1.63,1.52,1.70,1.68,1.57]
        prom_edad=(sum(edad))/len(edad)
        prom_peso=(sum(peso))/len(peso)
        prom_estatura=(sum(peso))/len(estatura)
        c=0
        x=0
        while c<8:
            x+=(edad.count(18+c))
            c+=1  
        c=1
        TreSeis=0  
        while c<150:
            TreSeis+=(edad.count(36+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso[contPos[0+c]]
            c+=1
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promdedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, personas con edad de entre [18-25] ")
        print(f"Hay {TreSeis}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")


#Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.         
  def ejercicio9(self):
        for i in range(0,7):
            for j in range(0, i+1):
                print("|" + str(i) + "|" + str(j) + "|")

#Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que la serie termina al leer un 0.          
  def ejercicio10(self):
      contador = 0
      suma = 0         
      numero = 1
      while numero !=0:
          numero = int(input("ingrese un numero entero (0 para termnar):"))
          if numero !=0:
             suma += numero
             contador +=1
      if contador ==0:
             print("no digito ningun numero.")
      else:
           promedio = suma / contador 
           print("El promedio de los {} numero es igual a {}.".format(contador,promedio))
          
   
  