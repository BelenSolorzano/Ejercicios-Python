# 1.	Determinar si un número entero proporcionado por el usuario es primo.
#  Un número primo es un entero que no tiene más divisores que él mismo y la unidad. 
class Número:
    def primo(self):
        pri = "T"
        divis = 2
        valor = int(input("Ingrese un número entero: "))
        while divis < valor and pri == "T":
            #* la respuesta sera evaluada si es o no primo en el proceso
            resp = valor % divis
            if resp == 0:
                pri = "F"
            divis = divis + 1
        #* en caso de estas correcto el ingreso imprime
        if pri == "T":
            print("El número {} es primo".format(valor))
        else:
            print("El número {} no es primo".format(valor))
#*Presentar
ingre = Número() 
ingre.primo()