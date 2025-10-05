def generaPares(limite):
    
    num=1
    
    while num<limite:
        yield num*2
        num=num+1
devuelvepares = generaPares(10)

    
    

print(next(devuelvepares))

def devuelve_ciudades(*ciudad):
    for elemento in ciudad:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas = devuelve_ciudades("Santo domingo","malecon")
print(ciudades_devueltas)
         


    