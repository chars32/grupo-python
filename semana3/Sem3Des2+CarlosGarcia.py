#Realizar una agenda de contactos; cuando inicie el programa que te pregunte si quieres 
#agregar contacto si se va a agregar un contacto, que pida nombre, telefono y e-mail; 
#cuando termines te vuelve a preguntar si quieres agregar contacto; si respondes no, 
#muestra la lista de contactos y termina.

nombres = []
telefonos = []
emails = []
cont = 0

def main():
	global cont
	pregunta = raw_input("Agregar Contacto s/n: ")
	print "-"*25
	return agregar(pregunta)
	
def agregar(pregunta):
	global cont
	while pregunta == "s":
		nombre = raw_input("Dame tu nombre: ")
		nombres.append(nombre)
		telefono = raw_input("Dame tu telefono: ")
		telefonos.append(telefono)
		email = raw_input("Dame tu email: ")
		emails.append(email)	
		cont += 1
		print ""
		return main()
	else:
		print ""
		print "Mi lista de Contactos"
		print "-"*25
		print "-"*25
		for x in range(cont):
			print "Nombre:",    nombres[x]
			print "Telefonos:", telefonos[x]
			print "Email:",     emails[x]
			print "-"*25
			print "-"*25
			
main()