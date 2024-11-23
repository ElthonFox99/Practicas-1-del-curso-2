horas=float(input("Cuantas horas trabaja"))
salario=float(input("Cuanto gana por hora"))
if(horas<40):
    salario_A=horas*salario
    print("Su salario es de: ",salario_A)
else:
    
    salario_B=horas*40*salario*1.5
    
    print("Su salario es de: ",salario_B)