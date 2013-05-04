#Ejercicio el cual nos da el numero de la tabla de multiplicar
#tambien nos da los limites para saber de donde a donde se multiplicara

def tabla_multiplicar():														#Definimos la funcion
	tabla = input("Dime hasta que tabla se debe multiplicar: ")					#Pedimos los valores en sus respectivas variables ...
	limite_inicial = input("Dime de que numero empezare a multiplicar: ")
	limite_final = input("Dime hasta que numero multiplicar: ")

	for i in range(1, tabla+1):													#Realizamos un ciclo for el cual recorra los valores de "tabla" empezando del valor 1
																				#y sumandole 1 al valor final "tabla", para que nos de los numeros correctos

		for x in range(limite_inicial, limite_final+1):							#Realizamos otro ciclo for anidado en el antrerior, el cual recorrera los valores de las
																				#variables "limite_inicial" , "limite_final" y a este ultimo le sumamos 1 para que imprima
																				#los valores correctos
			multi = i*x															#declaramos una valor "multi" la cual contendra el resultado de la multiplicacion por cada ciclo
			
			print i, "*", x, "=", multi 										#imprimimos resultado

		print "-----------"													

tabla_multiplicar()