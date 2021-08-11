#Registro de usuarios COVID
#Examen final Estructura de datos y algoritmos I
#Avalos Jasso José Carlos
# Grupo 15 Semestre 2021-2
op='0' #Se asigna un valor 0 a op(opción)
datos=[] #Én esta parte es el inicio y el registro de datos
pc=0     #Pc es el contador para las personas infectadas
pce=0    #Pce es el promedio de la edad de las personas contagiadas
while(op!='2') :    #Abertura del menú para el programa
	print(" 1)Llenar\n 2)Salir")   #Elección de las 2 posibles opciones, el llenar la base de datos y el salir
	op=input("Elige una opción: ")  
	if op=='1':               #Opción 1 la cuál es llenar el formulario
		ed=input("Edad de la persona: ")       #Ingreso de edad de los pacientes
		rc=input("Rango COVID [0-1] ")         #Ingreso de rango de edad de covid de los pacientes
		if float(rc)>=0.8:                     #Si el paciente tiene el rango es igual o mayor a 0.8, el paciente es positivo
			pc=pc+1                            		#El contador de las personas contagiadas aumenta en 1
			pce=pce+int(ed)                         #El promedio de la edad de las personas contagiadas aumenta
		reg=ed+','+rc+'\n'                     #Los datos y la información (Edad y rango covid)
		datos.append(reg)                      #Esto mismo se cambia por una función llamada "datos"
	elif op=='2':                              #Opción 2 salir del programa
		print("Gracias por usar mi programa")  #Mensaje de despedida del programa
	else:
		print("Opción no valida")              #Mensaje de invalidación de datos ingresados
print (datos)                              #Impresión de la función con los datos almacenados
a=open("bd.csv","a")                       #Creación de un archivo excel en donde se almacenan los datos registrados y se almacenan por columnas 
a.writelines(datos)                        #Escritura y almacenamiento de datos almacenados
a.close()                                  #Cierre de archivo
#Determinación del semaforo según la cantidad de personas contagiadas
if pc==0:                                  
	print("El semaforo se encuentra en verde, no hay infectados")
elif pc>=1 and pc<=30:
	print("El semaforo se encuentra en amarillo")
elif pc>=31 and pc<=70 :
	print("El semaforo se encuentra en naranja")
elif pc>=71 and p<=100:
	rint("El semaforo se encuentra en rojo, por favor no salga")

#Demostración de los datos almacenados
a=open("bd.csv","r")
contenido=a.read()
a.read()
a.close()
print(contenido)
pce=pce/pc #Calculo e impresión del promedio de la edad de las personas infectadas
print("El promedio de edad de los infectados es igual a",pce)