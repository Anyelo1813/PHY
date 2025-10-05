for i in ["mateo","camila","natalia"]: #bucle co instruccion in para que recorra la lista imprimiendo la cantidad de valores que tenga
    #print("HOLA",end=" ") #end para dejar espacio en blanco y no haga salto de linea
    
for i in "anyelodelarosa821@gmail.com": #Con este bucle tambien se pueden recorrer cadenas de strings como este ejemplo
    print("Hola mundo",end="  ")
    

email=False
for i in "anyelodelarosa214@gmail.com": 
    
    if i=="@":
        email=True
if email == True :
    print("El corre es correcto porque tiene arroba")
else:
    print("El correo es incorrecto porque no tiene @")
    


for  i in range(10):
    print(f"valor de la variable  {i}")
    
    
for i in range(10,41,3): # el primer argumento vendria siendo el numero incial, el 40 hasta donde termine y el tercero de cuanto en cuanto
    print(i)
    