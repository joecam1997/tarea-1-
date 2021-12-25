#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho 
#número.

if __name__ == '__main__':
     print("Ingrese Número del Mes (1 - 12) : ")
     num = int(input())
     if num==1:
          print("ENERO")
     elif num==2:
          print("FEBRERO")
     elif num==3:
          print("MARZO")
     elif num==4:
          print("ABRIL")
     elif num==5:
          print("MAYO")
     elif num==6:
          print("JUNIO")
     elif num==7:
          print("JULIO")
     elif num==8:
          print("AGOSTO")
     elif num==9:
          print("SETIEMBRE")
     elif num==10:
          print("OCTUBRE")
     elif num==11:
          print("NOVIEMBRE")
     elif num==12:
          print("DICIEMBRE")
     else:
          print("NÚMERO DEL MES INCORRECTO")