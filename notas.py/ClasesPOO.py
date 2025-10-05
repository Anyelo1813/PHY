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