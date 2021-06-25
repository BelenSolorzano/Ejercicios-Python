#1.	Calcular el factorial de N números enteros leídos de teclado. 
class Factorial:
    def numero(self ):
            #*Pedido y evaluacion de valores ingresados
            valor = int(input("Ingrese un número: "))
            factor = 1
            if valor != 0: 
                for m in range(1, valor + 1):
                    factor = factor * m
            print("El factorial del número",valor, "es : ",factor)
#*Presentar 
fac = Factorial()
fac.numero()