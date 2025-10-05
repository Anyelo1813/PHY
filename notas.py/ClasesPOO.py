""""
class tv():
    Altura=30
    ancho=15
    color="negra"
    Estado="Apagada"
    
    def encender(self):
        self.Estado="Encendida"
        
    def estado2(self):
      if(self.Estado == "Encendida"):
        return print("El tv esta Encendido")
        
      else:
            return print("El tv se encuentra apagado")
        
        

mitv=tv()
print("El color de mi TV es :",mitv.color)
mitv.encender()
print( mitv.estado2()) 
"""
class coche:
  
  def __init__(self):   #Constructor
  
    self.largochasis=250
    self.anchochasis=120
    self.__ruedas=4    #Encapsulamiento 
    self.enmarcha=False
  
  
  def arrancar(self,arrancancamos):
    self.enmarcha = arrancancamos
    if(self.enmarcha):
        return print("El coche esta en marcha")
        
    else:
        return print("El coche esta parado")
      
  def estado(self):
    print("El coche tiene",self.anchochasis,self.largochasis,"De largo",self.__ruedas,"Ruedas")
      

micoche = coche()
micoche.arrancar(False)
micoche.estado()
micoche.ruedas=3
