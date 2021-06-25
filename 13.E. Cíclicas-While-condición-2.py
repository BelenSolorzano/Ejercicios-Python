# 2.	Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por centinela. 
class Centinela:
    def números (self):
        sumar = 0
        pro = 1
        valorn = int(input("Ingrese un número  o (-1 )para finalizar ingreso: "))
        #*Proceso de evaluacion de ingreso
        while valorn != -1 :
            sumar = sumar + valorn
            pro = pro * valorn
            #*Pide los valores numericos a ingresar mostrando la opcion de finalizarlo a partir del ingreso de -1 
            valorn = int(input("Ingrese un número  o (-1 )para finalizar ingreso: "))
        print("La suma de los números es: {}".format(sumar))
        print("El producto de los números es: {}".format(pro))
#*  Presentar
cen = Centinela()
cen.números()



