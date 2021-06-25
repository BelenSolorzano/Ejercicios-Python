# 1.	Determinar la cantidad de dinero que recibirá un trabajador por concepto de 
# las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo 
# exceden de 40, el resto se consideran horas extras y que éstas se pagan al doble 
# de una hora normal cuando no exceden de 8; si las horas extras exceden de 8 se pagan
#  las primeras 8 al doble de lo que se paga por una hora normal y el resto al triple.  
class Trabajador:
    def salario(self): 
        horasT = int(input("Ingrese horas trabajadas: "))
        pxHora = float(int(input("Ingrese el valor a pagar por horas de trabajo: $ ")))
        if  horasT > 40:
            hExtra = horasT - 40
            #*Calcula las hora sobrepasadas a las 48 permitidas calculando el triple del pago
            if hExtra > 8 : 
                sobrepaso = hExtra - 8  
                pago = (pxHora * 2)*8 + (sobrepaso * 3 )* sobrepaso 
                print("El trabajador tiene", sobrepaso ," horas extras, su salario triple es: $ {:.2f}".format(pago)) 
            #*Calcula el doble por mantenerse entre los 40 y 48 de horas laborales
            else:
                pago = (pxHora * 2) * hExtra
                salarioT = (pxHora * 40 )+ pago 
                print("El trabajador tiene un doble de su pago por hora, su salario total es de: $ {:.2f}".format(salarioT))
        #*En caso de que las horas sean menores a 40 se mentiene el sueldo por el valor por horas trabajadas
        else:
            salarioT = horasT * pxHora 
            print ("El pago total al trabajador es : $ {:.2f} ".format(salarioT))
#*Presentar
su = Trabajador()
su.salario()     
