def main():
	f = input("Cuanto cuesta 1 segundo de comunicacion: ")
	n = input("Cuantas comunicaciones hubo: ")
	for x in range(n):
		hs = input("Cuantas horas?: ")
		mins = input("Cuantos minutos?: ")
		seg = input("Cuantos segundos?: ")
		segcalc = asegundos(hs, mins, seg)
		costo = segcalc * f
		print "Duracion: ", segcalc, "segundos. Costo: ",costo, "$"

def asegundos(horas, minutos, segundos):
	segsal = 3600 * horas + 60 * minutos + segundos
	return segsal

main()
