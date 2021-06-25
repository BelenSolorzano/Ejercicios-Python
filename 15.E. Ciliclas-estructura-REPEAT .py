# 1.	Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N 
# y calcular el resultado de la siguiente serie: 1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. 
# Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.   
class Entero:
    def número(self):
        #*Variables
        Seri = 0 
        m = 1
        valor = int(input("Ingrese un número entero: "))
        bandera = " T "
        #*Proceso
        while m < valor:
            if bandera == "T": 
                Seri = Seri + ( 1 / m)
                bandera = "F"
            else:
                Seri = Seri - ( 1 / m)
                bandera = "T"
            m = m + 1  
        print("Serie:{}".format(Seri))
#*Presentar
num = Entero()
num.número()

