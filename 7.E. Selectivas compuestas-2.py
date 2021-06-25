#2.	Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres. 
class Números:
    def comparación(self):
        #*pedir el ingreso de los numeros por teclado
        num1 = int(input("Ingrese primer número: "))
        num2 = int(input("Ingrese segundo número: "))
        num3 = int(input("Ingrese tercer número: "))
        #*Proceso de comparación 
        if num1 > num2 and num1 > num3 :
            mayor = num1
            print("El número", num1," es el mayor de los números".format(mayor))
        elif num2 > num3:
            mayor = num2
            print("El número", num2," es el mayor de los números".format(mayor))
        else:
            mayor = num3
            print("El número", num3," es el mayor de los números".format(mayor)) 
#*Presentar
num = Números()
num.comparación()