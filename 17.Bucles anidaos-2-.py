# 2.	Sea un vector “Calificaciones” de 100 componentes: En forma de columna se representaría así: 
  
# Para acceder a valores específicos del arreglo, use un valor de índice que apunte al elemento deseado. 
# Por ejemplo, para acceder al primer elemento del arreglo calificaciones debe utilizar el valor de índice 0 (calificaciones[0] ).
# INICIALIZACIÓN Y ASIGNACIÓN DE VALORES
# Como se decía anteriormente, antes de utilizar un arreglo es necesario inicializarlo:
#            Calificaciones [0];
# Para inicializar todos los elementos de una vez, se colocan dentro de un bucle, comúnmente una estructura For 
# que va del primer elemento al último que contiene el arreglo.
# Para asignar un valor a un elemento del arreglo se hace, por ejemplo:
#            Calificaciones [0] = 100;
# Cuando se usan arreglos, una operación común es usar una variable índice para acceder a los elementos de un arreglo.
# Suponiendo que la variable índice I contiene el valor 3, la siguiente instrucción asigna el valor 400 a valores [3]:
#            valores[I]   =   400;

class Vectores:
    def Calificaciones(self):
        #*variables
          cali = []
          l = 0
          m = 1
          #*Proceso
          for r in range(0,100,1):
            calificaciones = int (input("Ingrese una calificación: "))
            cali.append(calificaciones)
            l = l + 1
          print("")
          for r in range (0,l,1):
            print("En Calificación {} es la nota de: {}".format(m,calificaciones[r]))
            m = m + 1 
#*Presentar
valor = Vectores()
valor.Calificaciones()