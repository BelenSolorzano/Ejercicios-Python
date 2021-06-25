#1.	Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100. 
class Número:
    def mostrar(self):
        l = 0
        #*Proceso por condición llevando contador (l)
        while l < 100:
            l = l + 1
            print(l ,"-",end=" ")
#*Presentar
n = Número()  
n.mostrar()     
