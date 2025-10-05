

import math


numero = int(input("Digite el numero"))
intentos = 0
while numero <0:
    print("no se puede encontrar la raiz de 0 o numero negativo")
    if intentos ==2:
        print("Su numero de intentos a acabado")
        break;
    
    numero=int(input("Digite el numero"))
    if numero<0:
        intentos = intentos+1
if intentos <2:
    solucion = math.sqrt(numero)
    print(solucion)
    

    
    
    