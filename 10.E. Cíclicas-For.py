#1.	Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado. 
class Primos:
    def cuadrados(self):
        sumatoria = 0 
        for b in range(1,101):
            cuadra = (b) * (b)
            sumatoria = sumatoria + cuadra
            #*mostrará por pantalla los numeros del 1 al 100 con su respectivo cuadrado
            print("El cuadrado de {} es = {}" .format(b,cuadra))
        print ("La suma de los cuadrados de los primeros 100 enteros es :{} ".format(sumatoria))
#*Presentar
total = Primos()
total.cuadrados()