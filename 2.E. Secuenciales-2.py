# 2.	Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
# que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones. 
class Vendedor:
    def Ganancias(self):
        #*Perdir al usuario ingreso de valores
        suelBase = float(input("Ingrese sueldo base del vendedor: $ "))
        venta1= float(input("Ingrese valor de primer venta del mes : $ "))
        venta2= float(input("Ingrese valor de segunda venta del mes : $ "))
        venta3= float(input("Ingrese valor de tercera venta del mes : $ "))  
        #*Cálculo de valores
        totVenta = venta1 + venta2 + venta3
        comi = totVenta * 0.10
        suelTotal = suelBase + comi              
        print("El 10% estra por comision del trabajador es de : $ {:.2f}".format(comi))
        print("El sueldo total del vendedor es de : $  {:.2f}".format(suelTotal)) 
#*Presentar
ven1 = Vendedor()
ven1.Ganancias()
          





         