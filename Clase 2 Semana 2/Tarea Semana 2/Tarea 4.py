num1=int(input("Digite un numero entero: "))
oper1=int(input("Elija un operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
if(oper1 == 1):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul+num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul-num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul*num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul/num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul**num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1+num2
        resul_2=resul%num3
        print("La suma de: ",num1," + ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")


elif(oper1 == 2):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul+num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul-num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul*num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul/num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul**num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1-num2
        resul_2=resul%num3
        print("La resta de: ",num1," - ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")
        
elif(oper1 == 3):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul+num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul-num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul*num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul/num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul**num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1*num2
        resul_2=resul%num3
        print("La multiplicacion de: ",num1," * ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")

elif(oper1 == 4):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul+num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul-num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul*num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul/num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul**num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1/num2
        resul_2=resul%num3
        print("La divicion de: ",num1," / ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")

elif(oper1 == 5):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul+num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul-num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul*num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul/num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul**num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1**num2
        resul_2=resul%num3
        print("El exponente de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")

    
elif(oper1 == 6):
    num2=int(input("Digite un segundo numero entero: "))
    oper2=int(input("Elija un segundo operador: \n.1 Suma \n.2 Resta \n.3 Multiplicacion \n.4 Divicion \n.5 Exponente \n.6 Modulo \n.Digite el numero de operador a usar: "))
    if(oper2 == 1):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul+num3
        print("El modulo de: ",num1," % ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"+",num3, " = ",resul_2)
        
    elif(oper2 ==2):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul-num3
        print("El modulo de: ",num1," % ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"-",num3, " = ",resul_2)
        
    elif(oper2 ==3):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul*num3
        print("El modulo de: ",num1," % ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"*",num3, " = ",resul_2)
        
        
    elif(oper2 ==4):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul/num3
        print("El modulo de: ",num1," % ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"/",num3, " = ",resul_2)
        
    elif(oper2 ==5):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul**num3
        print("El modulo de: ",num1," % ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"**",num3, " = ",resul_2)
        
    elif(oper2 ==6):
        num3=int(input("Digite un tercer numero entero: "))
        resul=num1%num2
        resul_2=resul%num3
        print("El modulo de: ",num1," ** ",num2," = ",resul,"\nLa segunda operacion es: ",resul,"%",num3, " = ",resul_2)

    else:
        print("Numero no valido")
    
    
else:
    print("Numero no valido")