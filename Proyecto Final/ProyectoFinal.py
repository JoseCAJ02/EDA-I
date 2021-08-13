#Registro de usuarios COVID Mejorado
#Proyecto final Estructura de datos y algoritmos I
#Avalos Jasso José Carlos
# Grupo 15 Semestre 2021-2
print("\t\t\tBienvenido a mi programa para crear una base de datos!!!")  #Mensaje de bienvenida
op='0' #Se asigna un valor 0 a op(opción)
datos=[] #Én esta parte es el inicio y el registro de datos
Infect="Infectado"           #Infect es la variable para ingresar como cadena el texto que señala la infección de las personas
NoInfect="No Infectado"      #NoInfect es la variable para ingresar como cadena el texto que señala las personas no infectadas
p=0      #P es el contador de las personas registradas
pc=0     #Pc es el contador para las personas infectadas
pce=0    #Pce es el promedio de la edad de las personas contagiadas
p1a10=0  #p1a10 es el contador de las personas con el rango de edad de 1 a 10
p11a20=0 #p11a20 es el contador de las personas con el rango de edad de 11 a 20
p21a30=0 #p21a30 es el contador de las personas con el rango de edad de 21 a 30
p31a40=0 #p31a40 es el contador de las personas con el rango de edad de 31 a 40
p41a50=0 #p41a50 es el contador de las personas con el rango de edad de 41 a 50
p51a60=0 #p51a60 es el contador de las personas con el rango de edad de 51 a 60
p61a70=0 #p61a70 es el contador de las personas con el rango de edad de 61 a 70
p71a80=0 #p71a80 es el contador de las personas con el rango de edad de 71 a 80
p81a90=0 #p81a90 es el contador de las personas con el rango de edad de 81 a 90
p91a100=0 #p91a100 es el contador de las personas con el rango de edad de 91 a 100
while(op!='2') :    #Abertura del menú para el programa
	print(" 1)Llenar\n 2)Salir")   #Elección de las 2 posibles opciones, el llenar la base de datos y el salir
	op=input("Elige una opción: ")  
	if op=='1':               #Opción 1 la cuál es llenar el formulario
		p=p+1                 #Incremento del contador de personas registradas
		ed=input("Edad de la persona: ")       #Ingreso de edad de los pacientes
		#Evaluación de los contadores por rango de edad
		if int(ed)>=1 and int(ed)<=10:
			p1a10=p1a10+1
		if int(ed)>=11 and int(ed)<=20:
			p11a20=p11a20+1
		if int(ed)>=21 and int(ed)<=30:
			p21a30=p21a30+1
		if int(ed)>=31 and int(ed)<=40:
			p31a40=p31a40+1
		if int(ed)>=41 and int(ed)<=50:
			p41a50=p41a50+1
		if int(ed)>=51 and int(ed)<=60:
			p51a60=p51a60+1
		if int(ed)>=61 and int(ed)<=70:
			p61a70=p61a70+1
		if int(ed)>=71 and int(ed)<=80:
			p71a80=p71a80+1
		if int(ed)>=81 and int(ed)<=90:
			p81a90=p81a90+1
		if int(ed)>=91 and int(ed)<=100:
			p91a100=p91a100+1
		rc=input("Rango COVID [0-1] ")         #Ingreso de rango de edad de covid de los pacientes
		if float(rc)>=0.8:                     #Si el paciente tiene el rango es igual o mayor a 0.8, el paciente es positivo
			pc=pc+1                            		#El contador de las personas contagiadas aumenta en 1
			pce=pce+int(ed)                         #El promedio de la edad de las personas contagiadas aumenta
			reg=ed+','+rc+Infect+'\n'           	#Los datos y la información ingresados en la variale registro con la persona infectada (Edad y rango covid)
		else:
			reg=ed+','+rc+NoInfect+'\n'       	    #Los datos y la información ingresados en la variale registro con la persona no infectada (Edad y rango covid)
		datos.append(reg)                      #Esto mismo se cambia por una función llamada "datos"
	elif op=='2':                              #Opción 2 salir del programa
		print("Gracias por usar mi programa")  #Mensaje de despedida del programa
	else:
		print("Opción no valida")              #Mensaje de invalidación de datos ingresados
print (datos)                              #Impresión de la función con los datos almacenados
a=open("bdm.csv","a")                       #Creación de un archivo excel en donde se almacenan los datos registrados y se almacenan por columnas 
a.writelines(datos)                        #Escritura y almacenamiento de datos almacenados
a.close()                                  #Cierre de archivo
#Determinación del semaforo según la cantidad de personas contagiadas
if pc==0:                                  
	print("El semaforo se encuentra en verde, no hay infectados")
	print("Hay",p,"personas registradas y ningún infectado")
elif pc>=1 and pc<=(p/4):
	print("El semaforo se encuentra en amarillo")
	print("Personas registradas:",p)
	print("Infectados:",pc)
elif pc>=(p/4)+1 and pc<=(p*.75) :
	print("El semaforo se encuentra en naranja")
	print("Personas registradas:",p)
	print("Infectados:",pc)
elif pc>=(p*.75)+1 and pc<=p:
	rint("El semaforo se encuentra en rojo, por favor no salga")
	print("Personas registradas:",p)
	print("Infectados:",pc)
#Demostración de personas registradas por rango de edad
if p1a10>0:
	print("Hay "+str(p1a10)+" personas dentro del rango 1 a 10")
else:
	print("No hay ninguna persona dentro del rango 1 a 10 años")
if p11a20>0:
	print("Hay "+str(p11a20)+" personas dentro del rango 11 a 20")
else:
	print("No hay ninguna persona dentro del rango 11 a 10 años")
if p21a30>0:
	print("Hay",p21a30,"personas dentro del rango 21 a 30")
else:
	print("No hay ninguna persona dentro del rango 21 a 30 años")
if p31a40>0:
	print("Hay",p31a40,"personas dentro del rango 31 a 40")
else:
	print("No hay ninguna persona dentro del rango 31 a 40 años")
if p41a50>0:
	print("Hay",p41a50,"personas dentro del rango 41 a 50")
else:
	print("No hay ninguna persona dentro del rango 41 a 50 años")
if p51a60>0:
	print("Hay",p51a60,"personas dentro del rango 51 a 60")
else:
	print("No hay ninguna persona dentro del rango 51 a 60 años")
if p61a70>0:
	print("Hay",p61a70,"personas dentro del rango 61 a 70")
else:
	print("No hay ninguna persona dentro del rango 61 a 70 años")
if p71a80>0:
	print("Hay",p71a80,"personas dentro del rango 71 a 80")
else:
	print("No hay ninguna persona dentro del rango 71 a 80 años")
if p81a90>0:
	print("Hay",p81a90,"personas dentro del rango 81 a 90")
else:
	print("No hay ninguna persona dentro del rango 81 a 90 años")
if p91a100>0:
	print("Hay",p91a100,"personas dentro del rango 91 a 100")
else:
	print("No hay ninguna persona dentro del rango 91 a 100 años")
#Demostración de los datos almacenados
a=open("bdm.csv","r")
contenido=a.read()
a.read()
a.close()
print(contenido)
pce=pce/pc #Calculo e impresión del promedio de la edad de las personas infectadas
print("El promedio de edad de los infectados es igual a",pce)