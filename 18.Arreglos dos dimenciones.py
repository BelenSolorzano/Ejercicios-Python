# 1.	Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos.
#  Los datos sobre estos exámenes se proporcionan de la siguiente manera: 
#  Cal1,1 Cal1,2 ............ Cal1,6
# Cal2,1 Cal2,2 ............ Cal2,6
# .......................
# Cal30,1 Cal30,2 ........ Cal30,6
# Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno i en el examen j. 
#   1 £ i £ 30, 1£ j £ 6
# Calcular lo siguiente:
# a)    el promedio de calificaciones de cada uno de los 6 exámenes
# b)    el promedio de cada alumno
# c)    el tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba también dicho promedio.

class Calificaciones:  
    def  dimensiones(self):
        cali =[]
        prom =[]
        #*Porceso de ingreso y evaluación por alumno y examen
        for l in range(30):
            cali.append([])
            for m in range(6):
                cali[l].append(None)
                cali[l][m] = float(input("Ingrese la calificación del alumno {} en el examen {}: ".format(l+1,m+1)))
        for l in range(30):
            for m in range(6):
                print(cali[l][m], end=" ")
            print() 
        for m in range(6):
            su = 0
            for l in range(30):
                su = su + cali[l][m]
            prom.append(su / len(cali))
            print("El promedio del examen {} es: {:.2f}".format(m + 1,su / len(cali)))
        for l in range(30):
            su = 0
            for c in range(3):
                su = su + cali[l][m]
            print("El promedio del alumno {} es: {:.2f}".format(l + 1, su / len(cali)))
        #*cáculo del promedio del examen mayor 
        examen = 0
        promMayor= prom[1]
        for m in range(3):    
            if promMayor < promMayor[m]:
                promMayor = promMayor[m]
                examen =m
        print("El examen {} obtuvo el mayor promedio siendo este: {}".format(examen + 1,promMayor))
#*Presentar
cal = Calificaciones()
cal.dimensiones()
 
 