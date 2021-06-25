# 1.	Dado como dato la calificación de un alumno en un examen, escriba “aprobado”
#  si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.   

class Alumno:
    def examen (self):
        nota = 0 
        nota = float(input("Ingrese nota de examen: ")) #*ingreso de notas con decimales en darse el caso
        #*Proceso condicion
        if nota >= 7 :
            print ("¡Aprobado!"," con una nota de: ",nota )
        else:
            print ("¡Reprobado!"," con una nota de: ",nota )
#*Presentar
notAlumno = Alumno()
notAlumno.examen()
