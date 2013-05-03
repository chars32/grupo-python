def binario_entero():
	#Definimos la funcion con la cual convertiremos los binarios a enteros
	numero = input("Ingresa el numero binario?: ")												#definimos una variable "numero" la cual almacenara el binaroio                       
	largo = len(str(numero))			                           								#definimos una variable "largo" para saber el largo de la variable "numero"
	total = 0											  						   				
	contador = 1																	

	for i in range(largo):																		#inicamos el ciclo "for" con un rango segun el largo de la variable "largo"
		constante = 1																			#declaramos la variable "constante" que nos ayudara a sumar uno al valor de contador
		numero = str(numero)																	#converitmos el valor de numero a string
		basedos = 2 ** i 																		#declaramos la variable basedos para sacar los exponentes en base dos
		suma = basedos * int(numero[largo-contador])											#definimos "suma" la cual contendra el valor de la suma + el valor de numero
		total = total + suma 																	#sumamos todo
		contador = contador + constante 														#aumentamos el contador
	print "Del numero binario ingresado: %s su numero entero es: %s" % (numero, total)

binario_entero()
