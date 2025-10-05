def division():
 #while True:
 
  try:
        
    op1=(float(input("Introduzca el primer digito")))
    op2=(float(input("Introduzca el segundo digito")))
    print("El resultado es "+str(op1/op2))
    
    #break
  except ZeroDivisionError:
     print("No se puede dividir entre 0")
 
  except ValueError:
     print("NO se puede escribir strings")

  print("calculo finalizado")



division()
    
    