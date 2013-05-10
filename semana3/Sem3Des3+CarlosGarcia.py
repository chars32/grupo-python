# escribir un algoritmo que me organize una lista de letras 
# en todas sus combinaciones posibles:

#a = ['a', 'b', 'c', 'd']

#resultado:
#('a', 'b'), ('a', 'c'), ('a', 'd'), 
#('b', 'a'), ('b', 'c'), ('b', 'd'), 
#('c', 'a'), ('c', 'b'), ('c', 'd'), 
#('d', 'a'), ('d', 'b'), ('d', 'c')

def lista_letras():
	letras = raw_input("Escribe las letras: ")
	largo = len(letras)

	for x in range(largo):
		letra = x
		resultado = 0
		for y in range(largo):
			if letra != y:
				print letras[x]+","+letras[y]
		print "--------"



lista_letras()