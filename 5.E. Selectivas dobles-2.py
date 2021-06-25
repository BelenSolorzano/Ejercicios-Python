# 2.	Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10%
#  si su sueldo es inferior a $600, en caso contrario no tendrá aumento. 
class Empleado:
    def salario(self):
        sueldo = 0 
        sueldo = float(input("Ingrese sueldo de empleado: $ " )) # Ingreso con decimales
        #*Proceso condicion
        if sueldo < 600 : 
            incre = sueldo * 0.10
            nuevoSueldo = sueldo + incre
            print ("El aumento del 10% en el salario es de: $ {:.2f}".format(incre) )
            print("EL nuevo sueldo del empleado es: $ {:.2f}" .format(nuevoSueldo))
        else:
            print ("El sueldo de empleado es: $ ",sueldo)
#*Presentar
suel= Empleado()
suel.salario()