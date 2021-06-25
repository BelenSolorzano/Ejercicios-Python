# 1.	Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen,
#  escriba "Aprobado" en caso que esa calificación es mayor o igual que 7. 
class Alumno:
    def calificación(self):
        calif = 0 
        calif = float(input("Ingrese nota de examen: ")) #por si el valor en esta con decimales
        #Proceso condicion
        if calif >= 7 :
            print ("Aprobado"," con una nota de: ",calif)
        else:
            return # no continuara ejecutando
#Presentar
nota = Alumno()
nota.calificación()
