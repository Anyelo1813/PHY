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
def arrancar(self,arrancancamos):
    self.enmarcha = arrancancamos
    if(self.arrancar):
     
     chqueking = self.chequeo()
    
    if(self.enmarcha and chqueking):
        return print("El coche esta en marcha")
    elif(self.enmarcha and chqueking==False):
          
      return print("Algo ha ido mal en el chequeo, no podemos arrancar")
        
    else:
        return print("El coche esta parado")
    def chequeo (self):
        print("Realizando chequeo interno")
    self.aceite="ok"
    self.puertas="cerradas"
    self.gasolina="ok"
     
    if(self.gasolina=="ok"and self.puertas=="cerradas" and self.aceite=="ok"):
       return True
     
    else:
       return False
    
      
  def estado(self):
    print("El coche tiene",self.anchochasis,self.largochasis,"De largo",self.__ruedas,"Ruedas")
      

micoche = coche()
print(micoche.arrancar(True))


