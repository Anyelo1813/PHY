print("EJERCICIO SOBRE NOMBRES PISA PAJAS")
print("ELIGE UN NOMBRE 1:RAFFY 2: COMANDANTE 3: EURY")

nombre_saludo = input("elige a quien quieres saludar")

greetings = 0
N=0
def saludo(sal):
    
    if sal == 1:
        greetings = "Tu baquero MAMIIIII" 
    if sal == 2:
            greetings= "COMANDO DEJE ESA HAMBRE DIO MIO..."
    if sal == 3 :
                
        greetings = "-3 por las medias"
    if (sal) == 4:
        greetings = 90
        
    if (greetings == 90):
        N = 8
        
                
    return greetings

if (N == 8):
    print("nuevo bloque de secuencias")
    print("MENU DE PIZZERIA")
    print("eliga una pizza del menu")
    print("1: PEPERONi" "2:Jamon y queso","3:vegetales","4:yaroas","5:empanadas")
    

print(saludo(int(nombre_saludo))) 
print(N)





