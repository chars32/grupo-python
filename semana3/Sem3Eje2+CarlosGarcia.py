#Hacer un metodo que reciba cuatro parametros, y devuelve el primero 
#por el segundo, el tercero entre el cuarto, y el segundo menos el tercero.

#funcionRara(10,5,6,3)
#(50,2,-1)

def funcionRara():
	lista = []
	lista2 = []
	print "Dame 4 numeros"
	print "---------------"
	for x in range(4):
		numero = input("Dame un numero: ")
		lista.append(numero)
	
	print ""
	print "tus numeros son:", lista
	
	lista2 = [(lista[0] * lista[1]), (lista[2] / lista[3]), (lista[1] - lista[2])]
	
	print "el resultado es:", lista2
	
funcionRara()