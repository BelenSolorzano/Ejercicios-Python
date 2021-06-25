# 1.	En una tienda se ofrece un descuento del 15% sobre el total de la compra 
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.    
class Tienda: 
    def cálculo(self):
     #*Perdir al usuario que ingrese valores
     totalc = float(input("Ingrese valor total en compra: $  ")) 
     #*cálculos de la compra
     descu = totalc * 0.15
     totalp = totalc - descu
     print ("Su total a pagar por compra es de $ {:.2f}  con un descuento de  $ {:.2f}".format(totalp,descu ))
     #*:.2f evitara que no imprima valores decimales muy largo
#*Presentar
llam1 = Tienda()
llam1.cálculo()