print("Elige que valoraacion quieres dar")
valo = input()

def condifional(calificacion):
    valoracion = "Exelente"
    
    if calificacion<5 :
        valoracion="Normal"
    return valoracion
    

print(condifional(int(valo)))



