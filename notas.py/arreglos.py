
arreglo=["grabiel","martin","ricardo","marcela","maria"]

arreglo.append("marcela") #se usa append para agregar un elemento al arreglo
arreglo.insert(1,"mariano") #En esta exprecion se utiliza lo que es el numero donde quieres agregar el elemento
arreglo.extend(["Angel","teodoro","Rafael"]) #con esta exprecion podemos agregar lo que serian varios, como concatenando otra lista
#arreglo.remove(["grabiel"]) #DE esta forma puedes remover un elemento de la lista 
arreglo.pop()# con esta funcion se puede elminar lo que es el ultimo elemento de la lista



print(arreglo.index("martin")) #De esta manera se puede buscar en que lugar esta el dato que quieres
print(arreglo[:]) #Forma de imprimir un valor del arreglo, se coloca el numero del lugar que quieres imprimir

print("pepe" in arreglo) #DE esta forma puedes buscar si equis elemento se encuentra en esa lista , devuelve true o false 



#      TUPLAS
mitupla=(18,18,"jose",2003)
# milista = list(mitupla)
#print(milista)   #DE esta forma puedes convertir una tupla en una lista

print(mitupla.count((18))) #De esta forma puedes averiguar cuantas veces se repite un valor en la tupla 

print(len(mitupla)) #DE esta forma puedes saber cuantos elementos tiene esa tupla


#diccionarios 

midccionario = {"Nombre":"Anyelo","Apellido":"De La Rosa","Edad":21}
print(midccionario["Nombre"])
print(midccionario.keys()) #DE esta forma puedes ver las claves de los diccionarios
print(midccionario.values()) #De esta forma puedes ver los valores de las claves 
print(len(midccionario)) #DE esta forma puedes ver el numero de valores que posee el diccionarios

