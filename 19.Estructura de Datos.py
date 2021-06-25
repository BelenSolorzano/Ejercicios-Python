# 1.	Aplicar las fases para la resolución de un problema para leer un vector de 20 números enteros y a continuación 
# escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores. 

class Vectores:
    def númerosEnteros(self):
        A = []
        B = []
        l = 0
        m = 0
        numero = []
        #*Petición y proceso de evaluación de ingreso
        for r in range (0,20,1):
            ingre = int(input("Ingrese un número entero porfavor:"))
            numero.append(ingre)
            if numero[r] < 0:
                A.insert(l,numero[r])                
                l = l + 1
            else:
                B.insert(m,numero[r])
                m = m + 1
        #*Presentar los valores de ingreso evaluados
        print("**************************************************")   
        for r in range(0,l,1):
              print("Vector A - El valor negativo es : {}".format(A[r]))
        print("**************************************************")   
        for r in range (0,m,1):
              print("Vector B - El valor positivo es : {}".format(B[r]))
#*Presentar      
valor = Vectores()
valor.númerosEnteros()  