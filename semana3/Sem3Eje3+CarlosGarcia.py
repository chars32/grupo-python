#Hacer un metodo que recibe un numero positivo, 
#y devuelve la suma de cada digito.
# ejemplo:     suma_digitos(1234)
# resultado:   10  (1 + 2 + 3 + 4)

def Suma_Digitos():
	lista = raw_input("Ingrese sus numeros: ")
	longitud = len(lista)
	acumulador = 0
	for i in range(longitud):
		acumulador = acumulador + int(lista[i])
	print "La suma es:", acumulador

Suma_Digitos()