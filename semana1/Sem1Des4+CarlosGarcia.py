#numero = input("Dame un numero: ")
numero = 4

acu_izq = ""
acu_der = ""
acu_sup = ""
acu_inf = ""

i = 3

"""for i in range(1, numero+1):
    espacio = ("_"*(numero-i))
    linea = espacio + acu_izq + str(i) + acu_der + espacio + "\n"
    acu_sup = acu_sup + linea"""


for i in range(numero-1, 0, -1):
    espacio_inf = ("_"*(numero-i))
    print espacio_inf
    linea_inf = espacio_inf + acu_izq + str(i) + acu_der + espacio_inf + "\n"
    acu_inf = linea_inf + acu_inf
        

    acu_izq = acu_izq + str(i)
    acu_der = str(i) + acu_der
    i += 1

print acu_inf





raw_input()