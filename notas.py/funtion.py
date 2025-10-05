
def mensaje():
    

    print("estamos aprendiendo python")
    print("estamos aprendiendo instrucciones basicas")
    print("poco a poco iremos avanzando")

mensaje()
mensaje()

#funcion con parametros y retorno de valores
def operacion(num1,num2):
    
    resultado = num1 + num2
    
    return resultado

almacena_resultado = operacion(10,20)
print(almacena_resultado)


    
def generaPares(limite):
    
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num=num+1
    return milista
    
print(generaPares(10))


