# 1.	Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por el usuario.  
class Números:
    def proceso(self):
        l = 1
        sum = 0
        #*Pedir por teclado la cantidad de numeros que va a ingresar
        opcion = int(input(" Ingrese cantidad de numeros a operar: "))
        #*Proeso condicionado
        while l <= opcion :
            #*Pedir los valores de cada  número
            numero = int(input("Ingrese un número: "))
            #*Suma
            sum = sum + numero
            l = l + 1
            #*Producto
            produ = sum * numero 
        print ("La suma de los numeros es: {}".format(sum))
        print ("El producto de los numeros es: {}".format(produ))     
#*Presentar
eva = Números()
eva.proceso()