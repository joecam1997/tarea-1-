#print("Ingresar horas laborables")
#segundos = float(input("Ingrese horas laborables : "))
#horas = int(segundos/3600)

#print("segundos  : ",segundos)

num=int(input("ingrese los segundos : "))
dias=(int(num/24))
hor=(int(num/60))
minu=int(hor*60)
seg=num-(hor*60)
print(str(hor)+"h "+str(minu)+"m "+str(seg)+"s" +str(dias))  
