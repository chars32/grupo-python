#En otras palabras, si deseas saber si un numero en una variable "x" es primo, 
#entonces ningun otro numero deberia poder dividir "x" 
#con residuo cero aparte del 1 y de x.

#--------- Ejercicio -------------------
#Escribe una funcion es_primo que tome un numero x como entrada y 
#devuelva el booleano Verdadero si x es primo y Falso si no lo es.

def es_primo():
	numero = input("Dame un numero: ")
	contador = 0
	lista = []
	verificador = True

	for i in range(1, numero+1):
		if (numero%i) == 0:
			lista.append(i)

	if len(lista) == 2:
		print lista
		print verificador
	else:
		verificador = False
		print lista
		print verificador

es_primo()