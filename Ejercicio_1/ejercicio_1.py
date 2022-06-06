" Ejercicio N° 1 "

import random

par = 0
impar = 0

for i in range(1000):
    n = random.randint(0, 100)
    if (n % 2) == 0:
        par += 1
    else:
        impar += 1

print(" Tenemos " + str(par) + " numeros pares " + " y " + str(impar) + " numeros impares ")