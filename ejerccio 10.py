#Todos los años que se dividen exactamente entre 400, o que son divisibles 
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
#Usando estas premisas crea un algoritmo que lea una fecha como un número 
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
#el mismo es un año bisiesto o no

while True:
    
  año = int(input('ingrese el año:\t'))
  
  yes = '%d es un año bisiesto.' % (año)
  no = '%d no es un año bisiesto.' % (año)
  
  if año % 400 == 0:
    print(si)
  
  elif año % 100 == 0:
    print(no)
  
  elif año % 4 == 0:
    print(si)
  
  else:
    print(no)
  
  print()