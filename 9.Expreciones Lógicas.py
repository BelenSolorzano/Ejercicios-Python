# 1.	Un ejemplo en el cual usamos el operador lógico AND sería:
# Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene
#  dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores 
#  que 80 en ambos exámenes es aceptado; en caso contrario es rechazado. 
class Aspirantes:
    def exámenes(self):
        #*Pedir las calificaciones de los examenes 
        C1 = int(input("Ingrese primera calificación: "))
        C2 = int(input("Ingrese segunda calificación: ")) 
        #*Proceso
        if (C1 > 80) and (C2 > 80) :
            print ("¡Excelente! Haz sido aceptado")
        else:
            print("¡Lo sentimos! Haz sido rechazado") 
#*Presentar
apro = Aspirantes()
apro.exámenes()