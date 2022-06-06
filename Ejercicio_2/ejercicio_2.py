" Ejercicio N° 2 "

m_siete = 0
m_nueve = 0

for n in range(1000 , 5001):
    if (n % 7) == 0:
        m_siete += 1
    elif (n % 9) == 0:
        m_nueve += 1

print("Hay " + str(m_siete) + " numeros multiplos de siete " + " y " + str(m_nueve) + " numeros multiplos de nueve ")