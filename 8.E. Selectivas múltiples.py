#1.	Diseñar un algoritmo tal que, dados como datos dos variables de tipo entero, 
#obtenga el resultado de la siguiente función: 
class Datos:
    def __init__(self):
         pass
    def variable(self):
        numero = float(input("Ingrese número entero entre (1/2/3): "))
        V = float(input("Ingrese valor cualquiera : "))
        Resp = 0
        #*Proceso / Evaluar ingresos 
        if numero == 1 :
            Resp = 100 * V
            print("El valor de la variable es: {:.2f}".format(Resp))
        else:
            if numero == 2 :
                Resp = 100 ** V
                print("El valor de la variable es: {:.2f} ".format(Resp))
            else:
                if numero == 3 :
                    Resp = 100 / V  
                    print("El valor de la variable es: {:.2f}".format(Resp))
                else:
                    Resp = 0 
                    print("El valor de la variable es: {}".format(Resp)) 
#*Presentar
resul = Datos()
resul.variable()