#Hacer un metodo que recibe un numero entero mayor o igual que 1 
#y devuelve el factorial (la multiplicacion desde 1 hasta el mismo numero)
# ejemplo: factorial(4)
# resultado: 24  (4 * 3 * 2 * 1)

def Factorial():
	lista = input("Ingrese su numero: ")
	acumulador = 1
	for i in range(1, lista+1):
		acumulador = acumulador * i 
	print "el factorial del numero", lista, "es", acumulador

Factorial()