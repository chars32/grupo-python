#Hacer un metodo que reciba como parametro un array de numeros (una lista) 
#y devuelva la multiplicaciones de todos ellos.
#      multiplicaLista([1,2,3,4])
#      resusltado = 24

def MultiplicaLista():
	lista = raw_input("Ingrese sus numeros: ")
	longitud = len(lista)
	acumulador = 1
	for i in range(longitud):
		acumulador = acumulador * int(lista[i])
	print "la multiplicacion de los numeros es:", acumulador

MultiplicaLista()
